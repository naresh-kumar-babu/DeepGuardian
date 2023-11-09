FROM python:3.8.7

USER 0

RUN mkdir /.cache

RUN chmod -R 777 /.cache

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

COPY . /app

RUN python manage.py makemigrations

RUN python manage.py makemigrations predictor

RUN python manage.py migrate

RUN python manage.py migrate predictor

CMD python manage.py runserver 0.0.0.0:8080
