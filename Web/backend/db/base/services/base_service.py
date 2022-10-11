from typing import TypeVar, Type, Optional, Tuple, List
from fastapi import HTTPException
from pydantic import BaseModel
from tortoise import models
from tortoise.functions import Trim

ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)


class BaseService:
    model: Type[ModelType]
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    query_schema: QuerySchemaType
    get_schema: GetSchemaType
    get_detail: GetSchemaType

    async def _get_create_fields_dict(self, schema):
        return schema.dict(exclude_unset=True)

    async def _replace_many_to_many_fields(self, scheme, obj):
        pass

    async def create(self, schema, *args, **kwargs) -> Optional[GetSchemaType]:
        obj = await self.model.create(**(await self._get_create_fields_dict(schema)), **kwargs)
        await self._replace_many_to_many_fields(schema, obj)
        return await self.get_schema.from_tortoise_orm(obj)

    async def update(self, schema, **kwargs) -> Optional[GetSchemaType]:
        await self.model.filter(**kwargs).update(**(await self._get_create_fields_dict(schema)))
        obj = self.model.get(**kwargs)
        await self._replace_many_to_many_fields(schema, await obj)
        return await self.get_schema.from_queryset_single(obj)

    async def delete(self, **kwargs):
        obj = await self.model.filter(**kwargs).delete()
        if not obj:
            raise HTTPException(status_code=404, detail='Запись не существует!')

    async def all(self) -> Optional[GetSchemaType]:
        return await self.get_schema.from_queryset(self.model.all())

    async def filter(
            self, limit=None, offset=None,
            order_by: Optional[List[str]] = None,
            annotations: Optional[List[Tuple[str, str, str]]] = None,
            pk_name: Optional[str] = None, **kwargs
    ) -> Optional[GetSchemaType]:
        query = self.model.filter(**{x: y for x, y in kwargs.items() if y is not None})
        if offset:
            query = query.offset(offset)
        if limit:
            query = query.limit(limit)
        if order_by:
            query = query.order_by(*order_by)
        elif pk_name is not None:
            query = query.order_by(pk_name)
        if annotations is not None:
            for response_field, db_field, prefetch in annotations:
                query = query.prefetch_related(prefetch).annotate(**{response_field: Trim(db_field)})
        return await self.get_schema.from_queryset(query)

    async def get(self, **kwargs) -> Optional[GetSchemaType]:
        return await self.get_detail.from_queryset_single(self.model.get(**kwargs))

    async def get_obj(self, **kwargs) -> Optional[ModelType]:
        return await self.model.get_or_none(**kwargs)
