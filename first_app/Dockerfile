FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /first_app/

COPY . /first_app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000
