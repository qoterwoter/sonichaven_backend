# Sonic Haven
Создание веб приложения для автоматизации бизнес процессов студии звукозаписи.

## Все API описаны в файле URLS.md

## Технологии

- [React]: библиотека JavaScript для создания пользовательских интерфейсов.
- [React-router-dom]: библиотека для маршрутизации страниц React.
- [Redux]: библиотека управления состоянием для приложений JavaScript.
- [Redux-Thunk]: библиотека для работы с асинхронным кодом в Redux.
- [Django]: веб-фреймворк Python высокого уровня.
- [Django REST framework]: набор инструментов для создания веб-API.
- [PostgreSQL]: система объектно-реляционных баз данных.

## Установка
Установите Python 3.x и pip на свой компьютер, если еще не установлены.

Создайте виртуальную среду Python с помощью venv командой
```sh
python -m venv venv
```
Активируйте виртуальную среду:
- на Windows: 
    ```
    venv\Scripts\activate
    ```
- На Unix или Linux:
    ```
    source venv/bin/activate
    ```
Клонируйте проект с GitHub:
```
git clone https://github.com/qoterwoter/sonichaved_backend.git
```
Перейдите в папку проекта:
```
cd sonichaved_backend
```
Установите зависимости, используя requirements.txt:
```
pip install -r requirements.txt 
```
Создайте базу данных:
```
python manage.py migrate
```
Создайте администратора:
```
python manage.py createsuperuser
```
Запустите сервер:
```
python manage.py runserver
```
Готово! Теперь вы можете перейти на http://localhost:8000 в вашем браузере и начать использовать приложение

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

[React]: <https://ru.reactjs.org>
[React-router-dom]: <https://reactrouter.com/en/main>
[Redux]: <https://redux.js.org/tutorials/quick-start>
[Redux-thunk]: <https://github.com/reduxjs/redux-thunk>
[Django]: <https://www.djangoproject.com>
[Django REST Framework]: https://www.django-rest-framework.org/
[PostgreSQL]: https://www.postgresql.org/