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

CMD python manage.py makemigrations

CMD python manage.py makemigrations predictor

CMD python manage.py migrate

CMD python manage.py migrate predictor

CMD python manage.py runserver 0.0.0.0:8080
