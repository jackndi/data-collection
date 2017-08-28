# Duka-connect
Data Collection Api

## Running the Production server

To run the `production` server clone the repository to your system and create the `.env` file as per the example `.env.example` . This file will contain information that is supposed to be secret. You should now be able to run the following command.

First install module not available in pip used to generate qrcode for two factor authenticaton.

* ``` pip install git+git://github.com/ojii/pymaging.git#egg=pymaging ```
*```pip install git+git://github.com/ojii/pymaging-png.git#egg=pymaging-png```

Then install pandas used to export data from django admin in format of `EXCEL`, `JSON`,`YAML`, `HTML`, `TSV`, `CSV`, `ODT` .

* ``` sudo apt-get install python-pandas ```

make sure to add swap memory for about 2GB as pandas requirements.
Create virtualenv and activate it run the following command.

```pip install -r requirements.txt```

```Python manage.py makemigration ?settings=settings.production```

```python manage.py migrate ?settings=settings.production```

```python manage.py createsuperuser ?settings=settings.production```

to start the server run

```python manage.py runserver ?settings=settings.production```

And run the unit test with the following command

```python manage.py test```

## Running Local develoment server

Don?t need to create `.env` file , just run the following command

```python manage.py makemigrations```

```python manage.py migrate```

```python manage.py createsuperuser```

```python manage.py runserver```


To read the API docs, make sure the server is running and visit the following link
* `http://localhost:8000/docs`

To access django admin visit
* `http://localhost:8000/admin`

To see the performance report of requests to the server
* `http://localhost:8000/monitor`