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


## PostgreSQL

https://artifacthub.io/packages/helm/bitnami/postgresql

- k8s

```shell
helm --namespace user-dlima --kubeconfig ~/.kube/qa.yaml install my-release oci://registry-1.docker.io/bitnamicharts/postgresql

```

- minikube

helm install my-release oci://registry-1.docker.io/bitnamicharts/postgresql

** Please be patient while the chart is being deployed **

PostgreSQL can be accessed via port 5432 on the following DNS names from within your cluster:

    my-release-postgresql.default.svc.cluster.local - Read/Write connection

To get the password for "postgres" run:

    export POSTGRES_PASSWORD=$(kubectl get secret --namespace default my-release-postgresql -o jsonpath="{.data.postgres-password}" | base64 -d)

To connect to your database run the following command:

    kubectl run my-release-postgresql-client --rm --tty -i --restart='Never' --namespace default --image docker.io/bitnami/postgresql:15.3.0-debian-11-r7 --env="PGPASSWORD=$POSTGRES_PASSWORD" \
      --command -- psql --host my-release-postgresql -U postgres -d postgres -p 5432

    > NOTE: If you access the container using bash, make sure that you execute "/opt/bitnami/scripts/postgresql/entrypoint.sh /bin/bash" in order to avoid the error "psql: local user with ID 1001} does not exist"

To connect to your database from outside the cluster execute the following commands:

    kubectl port-forward --namespace default svc/my-release-postgresql 5432:5432 &
    PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d postgres -p 5432

WARNING: The configured password will be ignored on new installation in case when previous Posgresql release was deleted through the helm command. In that case, old PVC will have an old password, and setting it through helm won't take effect. Deleting persistent volumes (PVs) will solve the issue.




- Plone chart

```shell
helm repo add plone https://plone.github.io/charts
```





kubectl --namespace user-dlima --kubeconfig ~/.kube/qa.yaml get pods

