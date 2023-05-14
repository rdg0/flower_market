# flower_market


### Скрипт

Скрипт для выборки продаж по прадавцам в разрезе покупателей находится тут:  

```
flower_market/market/sales.py
```


### Стек:

Python 3.8  
Django 4.1

### Запуск  


Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:rdg0/flower_market.git
```

```
cd flower_market
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Перейти в каталог market:  

```
cd market
```

Выполнить миграции:

```
python3 manage.py migrate
```  

Создать суперпользователя


```
python3 manage.py createsuperuser
```  


Запустить проект:

```
python3 manage.py runserver
``` 

Через панель администратора заполнить модели.



Для запуска скрипта выборки продаж выполнить:

```
python3 sales.py
``` 

