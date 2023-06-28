# CERRADO SPRINT

Anotações da participação no evento CERRADO SPRINT, realizado no TSE no período de 26 a 28 de junho de 2023.

## Ambiente - todos os projetos

- IDE

- Docker

- Python

- Nodes 16 (nvm)

### Preparando

```shell
nvm use 16
npm install -g yo

caso tenhas o yanr instalado (apt)
sudo apt remove cmdtest
sudo apt remove yarn

npm install -g yarn
yarn --version

sudo apt install python3.10
```

## PloneGov-Br

https://github.com/plonegovbr

### Projetos para contribuição

- https://github.com/plonegovbr/portal-brasil

```shell
git clone git@github.com:plonegovbr/portal-brasil.git

cd portal-brasil

make install-backend

make start-backend

make install-frontend

make start-frontend
```

## Plone 6

- Instalação do plone 6 através de pacotes (fonte: https://6.docs.plone.org/install/install-from-packages.html)

```shell
python3 -m venv ~/.venv-plone6
source ~/.venv-plone6/bin/activate

pip install --upgrade cookiecutter

cookiecutter https://github.com/collective/cookiecutter-plone-starter

cd plone6-cerrado (craido no passo anterior)

make install

make start-backend

make start-frontend
```

- URLs

http://localhost:8080/Plone/

http://localhost:3000/


## Consumo de API

Fonte: https://6.docs.plone.org/plone.restapi/docs/source/index.html

### Por linha de comando

- Recuperando informações do site:

```shell
curl -i -X GET http://localhost:8088/Plone -H "Accept: application/json" --user admin:admin

- Criar uma pagina com short-name front-page. Depois consultar:

curl -i -X GET http://localhost:8088/Plone/front-page -H "Accept: application/json" --user admin:admin

- Autenticando com token e depois usando o token

curl -i -X POST http://localhost:8088/Plone/@login -H "Accept: application/json" -H "Content-Type: application/json" --data-raw '{"login": "admin", "password": "admin"}'

curl -i -X GET http://localhost:8088/Plone -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY4Nzk0MDE3OCwiZnVsbG5hbWUiOm51bGx9.idHaTGM4W2Zue-cp4EdPgjp9S4Vjzfag5s8PittelTI"

- renovando token, para recuperar outro

curl -i -X POST http://localhost:8088/Plone/@login-renew -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY4Nzk0MDE3OCwiZnVsbG5hbWUiOm51bGx9.idHaTGM4W2Zue-cp4EdPgjp9S4Vjzfag5s8PittelTI"
```

### usando python

Consultar os arquivos:

- api-autenticacao.py
