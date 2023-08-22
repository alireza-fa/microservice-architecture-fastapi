FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

WORKDIR /third_app/

COPY . /third_app/

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8002
