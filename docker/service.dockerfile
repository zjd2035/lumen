FROM python:3.7.3-alpine3.9

WORKDIR /app

RUN apk add --no-cache gcc musl-dev linux-headers bash

COPY requirements.txt requirements.txt

RUN python3 -m venv venv && source venv/bin/activate
RUN pip install -r requirements.txt

CMD cd app
CMD ["flask", "run"]
