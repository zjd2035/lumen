FROM python:3.7.3-alpine3.9

WORKDIR /code

ENV FLASK_APP lumen/app.py
ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc musl-dev linux-headers bash

COPY requirements.txt requirements.txt

RUN python3 -m venv venv && source venv/bin/activate
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run"]
