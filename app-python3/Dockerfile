FROM python:3.9

RUN apt-get update
RUN apt install -y vim

# This prevents python from generatring the directory "__pycache__"
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
