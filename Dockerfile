FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_APP=app:create_app

EXPOSE 80

ADD . /app
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]