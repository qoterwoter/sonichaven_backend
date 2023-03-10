# Sonic Haven
Создание веб приложения для автоматизации бизнес процессов студии звукозаписи.

## Технологии

Dillinger uses a number of open source projects to work properly:

- React: библиотека JavaScript для создания пользовательских интерфейсов.
- Redux: библиотека управления состоянием для приложений JavaScript.
- Django: веб-фреймворк Python высокого уровня.
- Django REST: набор инструментов для создания веб-API.
- PostgreSQL: система объектно-реляционных баз данных.

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

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
