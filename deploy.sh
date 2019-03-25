#!/bin/bash

echo "Deploying "hello-world" Python flask application"
kubectl create -f hello-world-deployment.yaml
kubectl create -f hello-world-service.yaml 

echo "Deploying "hello-world-reverse" Python flask application"
kubectl create -f hello-world-reverse-deployment.yaml
kubectl create -f hello-world-reverse-service.yaml 
