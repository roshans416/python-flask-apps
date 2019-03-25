FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python3.7", "hello-world-app-reverse.py"] 
CMD ["127.0.0.1", "8080"]
