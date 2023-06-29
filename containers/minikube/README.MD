# Minkube

Fontes:

- https://minikube.sigs.k8s.io/docs/start/

- https://kubernetes.io/pt-br/docs/tutorials/hello-minikube/

 
## Instalação no ubuntu




```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb

sudo dpkg -i minikube_latest_amd64.deb
```

## Uso

- Iniciar

```shell
minikube start
```
- Integragir

```shell
kubectl get po -A

minikube kubectl -- get po -A
```
- deploy de aplicação

1. service

```bash
kubectl create deployment hello-minikube --image=kicbase/echo-server:1.0

kubectl expose deployment hello-minikube --type=NodePort --port=8080
```