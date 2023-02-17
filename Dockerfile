FROM python:latest

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY . /decor
WORKDIR /decor

RUN pip install -r requirements.txt

EXPOSE 80

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]