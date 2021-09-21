FROM python:3.8.0b3-alpine3.10

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app

EXPOSE  80

CMD ["python", "app.py"]