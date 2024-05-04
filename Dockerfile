FROM python:alpine

RUN apk --update-cache add \
    gcc \
    g++ \
    build-base \
    linux-headers \
    python3-dev \
    pcre-dev

RUN pip install --upgrade pip \
    && pip install --no-cache-dir \
    Flask \
    uwsgi

COPY . /app
WORKDIR /app

ENV FLASK_APP=src/server.py

EXPOSE 3031

# CMD ["uwsgi", "--ini", "/app/src/uwsgi.ini"]
CMD ["flask", "run", "--host=0.0.0.0", "--port=3031"]