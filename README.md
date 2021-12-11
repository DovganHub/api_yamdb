# api_yamdb
api_yamdb
#eto readme
# api_yamdb
## Создаём и активируем виртуальное окружение:
python3 -m venv venv
source venv/Scripts/activate
## Ставим библиотеки:
pip install -r requirements.txt --вжух
## Производим миграции:
python manage.py makemigrations
python manage.py migrate
## Стартуем:
python manage.py runserver
