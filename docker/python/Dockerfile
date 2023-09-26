FROM python:3.11

COPY ./secret_guide /srv/www/secret_guide
COPY ./.env /srv/www/secret_guide/secret_guide
WORKDIR /srv/www/secret_guide

RUN pip install --no-cache-dir --upgrade -r requirements.txt