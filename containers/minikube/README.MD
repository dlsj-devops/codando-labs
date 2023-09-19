# Minkube

Fontes:

- https://minikube.sigs.k8s.io/docs/start/

- https://kubernetes.io/pt-br/docs/tutorials/hello-minikube/

 
## Instalação no ubuntu


```bash
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube_latest_amd64.deb

sudo dpkg -i minikube_latest_amd64.deb
```

## Uso (https://minikube.sigs.k8s.io/docs/start/)

- Iniciar

```shell
minikube start
```
- Interagir

```shell
kubectl get po -A

minikube kubectl -- get po -A

kubectl get namespace
```

- Craindo namespace para trabalho

```bash
kubectl create namespace nsteste
```

- Deploy de aplicação

1. service

Criando um serviço e expondo pela porta 8080

```bash
kubectl --namespace nsteste create deployment hello-minikube --image=kicbase/echo-server:1.0

kubectl --namespace nsteste expose deployment hello-minikube --type=NodePort --port=8080

kubectl --namespace nsteste port-forward service/hello-minikube 7080:8080
```

2. LoadBalancer

```bash
kubectl --namespace nsteste create deployment balanced --image=kicbase/echo-server:1.0

kubectl --namespace nsteste expose deployment balanced --type=LoadBalancer --port=8090

kubectl --namespace nsteste get services balanced

#outro terminal
minikube tunnel

kubectl --namespace nsteste get services balanced
```

3. Ingress

Habilitando o ingress no minikube:

```shell
minikube addons enable ingress
```

Criando dois serviços echo-service e um ingress que depedendo do path, direciona para o serviço correto:

```yaml
kind: Pod
apiVersion: v1
metadata:
  name: foo-app
  labels:
    app: foo
spec:
  containers:
    - name: foo-app
      image: 'kicbase/echo-server:1.0'
---
kind: Service
apiVersion: v1
metadata:
  name: foo-service
spec:
  selector:
    app: foo
  ports:
    - port: 8080
---
kind: Pod
apiVersion: v1
metadata:
  name: bar-app
  labels:
    app: bar
spec:
  containers:
    - name: bar-app
      image: 'kicbase/echo-server:1.0'
---
kind: Service
apiVersion: v1
metadata:
  name: bar-service
spec:
  selector:
    app: bar
  ports:
    - port: 8080
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
spec:
  rules:
    - http:
        paths:
          - pathType: Prefix
            path: /foo
            backend:
              service:
                name: foo-service
                port:
                  number: 8080
          - pathType: Prefix
            path: /bar
            backend:
              service:
                name: bar-service
                port:
                  number: 8080
---
```

Criando os serviços e o ingress:

```shell
kubectl --namespace nsteste apply -f exemplo-services-ingresss.yml
```
Consultando os ingress:

```bash
kubectl --namespace nsteste get ingress

curl [address-ingress]/foo
Request served by foo-app


curl [address-ingress]/bar
Request served by bar-app
```

4. Gerenciando o minikube / cluster



minikube pause

minikube unpause

minikube stop


efeito apenas quando se cria o cluster

minikube config set memory 2048


lista dos addons

minikube addons list

criando um novo cluster chamado cteste (subira com memória de 2048MB)

minikube start -p cteste --kubernetes-version=v1.16.1

apagando o cluster cteste

minikube delete cteste


## Uso (https://kubernetes.io/pt-br/docs/tutorials/hello-minikube/)