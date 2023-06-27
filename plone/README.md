# Descrição

Algumas anotações sobre o CMS Plone, usado no TRE.

## Anotações

- Fonte

```url
https://github.com/plone/plone.docker
```

- Docker (Plone 5.* em Debian)

```bash
docker run -d --name plone5 -p 8088:8080 plone
```

- Acesso

```url
http://localhost:8080
```

## Plne 6 demo

https://github.com/collective/plone6-local-demo

## Instalação do plone 6

- por pacotes

https://6.docs.plone.org/install/install-from-packages.html

- por containers

https://6.docs.plone.org/install/containers/index.html


- URLs

http://localhost:8088/Plone/

http://localhost:3000/


### API

- Recuperando informações do site:

curl -i -X GET http://localhost:8088/Plone -H "Accept: application/json" --user admin:admin

- Criar uma pagina com short-name front-page. Depois consultar:

curl -i -X GET http://localhost:8088/Plone/front-page -H "Accept: application/json" --user admin:admin

- Autenticando com token e depois usando o token

curl -i -X POST http://localhost:8088/Plone/@login -H "Accept: application/json" -H "Content-Type: application/json" --data-raw '{"login": "admin", "password": "admin"}'

curl -i -X GET http://localhost:8088/Plone -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY4Nzk0MDE3OCwiZnVsbG5hbWUiOm51bGx9.idHaTGM4W2Zue-cp4EdPgjp9S4Vjzfag5s8PittelTI"

- renovando token, para recuperar outro

curl -i -X POST http://localhost:8088/Plone/@login-renew -H "Accept: application/json" -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY4Nzk0MDE3OCwiZnVsbG5hbWUiOm51bGx9.idHaTGM4W2Zue-cp4EdPgjp9S4Vjzfag5s8PittelTI"