Запуск с Docker-compose:
- docker-compose up --build -d

<br>

Запуск без Docker:
- uvicorn main:app -reload

<br>

Просмотр документации на локальном сервере:
- http://127.0.0.1/docs

<br>
    
Nginx: 
- Настройки веб сервера

<br>
    
Scripts:
- Скрипты для развертывания

<br>

Создание миграций:
- $ docker-compose exec web aerich migrate
- $ docker-compose exec web aerich upgrade