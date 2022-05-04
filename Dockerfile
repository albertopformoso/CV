FROM python:3.8

WORKDIR /usr/app

COPY /src ./src
COPY .env .
COPY app.py .
COPY Procfile .
COPY requirements.txt .

RUN apt-get update
RUN python -m pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]