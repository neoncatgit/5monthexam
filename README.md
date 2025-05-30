#  Blog API  #

 Это REST API для блога на Django и Django REST Framework.
Поддерживается регистрация, авторизация, создание постов и комментариев.
База данных: PostgreSQL.
Есть поддержка Docker. 

⸻

#  Как запустить без Docker:  #
 1. Установить зависимости:
pip install -r requirements.txt
 2. Настроить подключение к PostgreSQL в settings.py
 3. Применить миграции:
python manage.py migrate
 4. Создать суперпользователя (по желанию):
python manage.py createsuperuser
 5. Запустить сервер:
python manage.py runserver

⸻

#  Как запустить с Docker:  #
 1. Собрать и запустить контейнеры:
docker-compose up --build
 2. В другом терминале применить миграции:
docker-compose exec web python manage.py migrate
 3. Создать суперпользователя (если нужно):
docker-compose exec web python manage.py createsuperuser
 4. Перейти на http://localhost:8000 чтобы проверить

⸻

Функции:
 1. Регистрация и авторизация через стандартные Django views
 2. Создание и редактирование постов (только автор может изменять)
 3. Комментарии к постам
 4. Пагинация (по 3 поста или комментария на страницу)
 5. Доступ к API только для авторизованных пользователей
 6. Документация по адресу /swagger/# doni.5month_control
# test5month2
