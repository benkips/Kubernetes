import os

print(os.popen('Starting Building of Docker Images ').read())

print(os.popen('docker build -t appdocker .').read())

print(os.popen('echo Building of Docker complete').read())

print(os.popen('echo Deployment to Kubernetes ').read())

print(os.popen('kubectl create  -f deployment.yml ').read())

print(os.popen('kubectl apply -f deployment.yml').read())

print(os.popen('kubectl get pods ').read())