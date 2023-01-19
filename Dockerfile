FROM python:3.7-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/backend

COPY ./requirements.txt /app/backend/requirements.txt

# Build psycopg2-binary from source -- add required required dependencies
#RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
#        pip install --no-cache-dir -r requirements.txt && \
#        apk --purge del .build-deps

RUN pip install -r requirements.txt

COPY ./dad/ /app/backend/

CMD [ "python", "manage.py", "migrate" ]
