FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip3 install flask psycopg2-binary==2.9.9
CMD ["python3", "app.py"]
