FROM python:3.10
EXPOSE 8080
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV DJANGO_SETTINGS_MODULE=blogapp.settings
ENV PYTHONPATH=$PYTHONPATH:/app

RUN python manage.py migrate

CMD python manage.py runserver


CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]