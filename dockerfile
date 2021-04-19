FROM tiangolo/uwsgi-nginx-flask
RUN pip install flask redis

COPY app2V1.py /app/main.py