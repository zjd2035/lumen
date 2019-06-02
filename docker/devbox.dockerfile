FROM python:3.7.3-alpine3.9

WORKDIR /app

# Installing client libraries and any other package you need
RUN apk update && apk add bash libpq

# Installing build dependencies
RUN apk add --virtual .build-deps gcc python-dev musl-dev postgresql-dev

COPY requirements.txt requirements.txt
COPY requirements-test.txt requirements-test.txt

RUN python3 -m venv venv && source venv/bin/activate
RUN pip install -r requirements.txt -r requirements-test.txt

# Delete build dependencies
RUN apk del .build-deps

CMD cd app
