# Instalação no ubuntu

```bash
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
heml version
```

# Repositório de charts

https://artifacthub.io/packages/search?kind=0


- PostgreSQL

https://artifacthub.io/packages/helm/bitnami/postgresql

```shell
helm --namespace user-dlima --kubeconfig ~/.kube/qa.yaml install my-release oci://registry-1.docker.io/bitnamicharts/postgresql
```

- Plone chart

```shell
helm repo add plone https://plone.github.io/charts
```





kubectl --namespace user-dlima --kubeconfig ~/.kube/qa.yaml get pods

