import os
import shutil
from datetime import datetime
from typing import Optional
from uuid import uuid4

from fastapi import UploadFile

from db.base.models import File
from db.base.schemas import GetFile


class FileService:
    def __init__(self, file: File):
        self.file = file

    @staticmethod
    def _get_file_name(postfix) -> str:
        if postfix in ['jpg', 'png', 'mp4']:
            filename = f'{uuid4()}.{postfix}'
        elif postfix == 'pdf':
            filename = f'{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}_{uuid4()}.{postfix}'
        else:
            raise FileService.WrongPostfix(postfix)

        return filename

    @staticmethod
    def _os_file_save(file, file_path):
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file, buffer)

    @staticmethod
    def _os_file_delete(file_path):
        os.remove(file_path)

    @staticmethod
    async def save_file(
            file: Optional[UploadFile],
            upload_folder: str,
            postfix: str
    ) -> GetFile:
        if file is None:
            raise FileService.FileNotExists()

        file_name = FileService._get_file_name(postfix)
        path = f'{upload_folder}/{file_name}'

        file_object = file.file

        FileService._os_file_save(file_object, path)

        new_file = await File.create(path=path)
        return await GetFile.from_tortoise_orm(new_file)


    async def delete_file(self):
        path_to_file = self.file.path
        await self.file.delete()
        self._os_file_delete(path_to_file)


    async def update_file(self, file: UploadFile, postfix: str) -> GetFile:
        path = self.file.path
        file_dir, _ = os.path.split(path)

        new_file_name = self._get_file_name(postfix)
        new_path = f'{file_dir}/{new_file_name}'

        self._os_file_save(file.file, new_path)
        await self.file.update_from_dict({"path": new_path})
        await self.file.save()
        self._os_file_delete(path)

        return await GetFile.from_tortoise_orm(self.file)


    class FileNotExists(Exception):
        def __init__(self):
            super().__init__("Файл не был передан")

    class WrongPostfix(Exception):
        def __init__(self, postfix):
            super().__init__(f"Был указан неверный постфикс {postfix}")



