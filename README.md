# python-flask-apps

**This repo consists of two Python Flask apps**

## hello-world-app

This simple Flask app when accessed will give "Hello World" JSON response. App files can be found under **python-hello-world/** directory. 

`hello-world-app.py`: Python flask file.

`Dockerfile`: To build Docker image for this app.

`requirements.txt`: List of Python libraries needed for the app.

#### How to deploy using Docker container?

```
docker build . -t python-hello-world:v1
docker run -itd -p 8080:8080 --name=hello-world python-hello-world:v1
```

## hello-world-app-reverse

This  app will accessed will connect to **hello-world-app** and displays the message field value in reverse format. App files can be found under **python-hello-world-reverse/** directory. 

`hello-world-app-reverse.py`: Python flask file.

`Dockerfile`: To build Docker image for this app.

`requirements.txt`: List of Python libraries needed for the app.

#### How to deploy using Docker container?

```
docker build . -t python-hello-world-reverse:v1

# Get the ip address of hello-world-app container
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}} hello-world 

docker run -itd -p 9080:8080 python-hello-world-reverse:v1 $IP_ADDR  8080
```
where,  
**IP_ADDR** is the IP Address of **hello-world-app**. Replace it with your value.

**8080** is the port number of hello-world-app.


## Deploy to K8S

**kubectl should be installed and configured to connect with a Kubernetes cluster**

Execute the following script.

```
./deploy_to_k8s.sh
```
This will create a deployment for "hello-world-app" and "hello-world-app-reverse". Also, both services will be exposed using service type "NodePort".

To access the services from browser

```
minikube service hello-world
minikube service hello-world-reverse
```
