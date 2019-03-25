#!/bin/bash

echo "Deploying "hello-world" Python flask application"
kubectl create -f k8s/hello-world-deployment.yaml
kubectl create -f k8s/hello-world-service.yaml 

echo "Deploying "hello-world-reverse" Python flask application"
kubectl create -f k8s/hello-world-reverse-deployment.yaml
kubectl create -f k8s/hello-world-reverse-service.yaml 
