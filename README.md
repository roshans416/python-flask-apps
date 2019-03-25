# python-flask-apps

**This repo consists of two Python Flask apps**

## hello-world-app

This simple Flask app when accessed will give "Hello World" JSON response. App files can be found under **python-hello-world/** directory. 

`hello-world-app.py`: Python flask file.

`Dockerfile`: To build Docker image for this app.

`requirements.txt`: List of Python libraries needed for the app.

### How to deploy using Docker container?

```
docker build . -t python-hello-world:v1
docker run -itd -p 8080:8080 --name=hello-world python-hello-world:v1
```

## hello-world-app-reverse

This  app will accessed will connect to **hello-world-app** and displays the message field value in reverse format. App files can be found under **python-hello-world-reverse/** directory. 

`hello-world-app-reverse.py`: Python flask file.

`Dockerfile`: To build Docker image for this app.

`requirements.txt`: List of Python libraries needed for the app.

### How to build Docker Image?

```
docker build . -t python-hello-world-reverse:v1

# Get the ip address of hello-world-app container
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} hello-world 

docker run -itd -p 9080:8080 python-hello-world-reverse:v1 $IP_ADDR  8080
```
where 
Replace **IP_ADDR** with the IP Address of **hello-world-app**
**8080** is the port number of hello-world-app


      
