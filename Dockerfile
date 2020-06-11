FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install flask flask-pymongo flask-wtf
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app


