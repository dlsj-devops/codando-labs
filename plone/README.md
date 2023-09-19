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

https://sixfeetup.com/blog/how-to-set-up-plone-6-using-docker

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

## Projetos e estudos

- Criar o esqueleto do projeto

https://www.cookiecutter.io/

https://github.com/collective/cookiecutter-plone-starter

- Testes

https://docs.pytest.org/en/7.3.x/contents.html#

- Fonte para design system (governo da Nova Zelândia)

https://www.digital.nsw.gov.au/delivery/digital-service-toolkit/design-system


- EEA

https://hub.docker.com/r/eeacms/plone

https://github.com/eea


##  dev

instalar pacotes adicionais:

./backend/mx.ini


efetuar testes

./bin/pytest src/plone6_cerrado/tests --disable-warnings

gerando imagens

make build-images

padrao: banco direto no postgresql


relstorage_dsn variavel de ambiente que passa os dados do postgresql

rodar como imagens / deploy

https://6.docs.plone.org/install/containers/images/backend.html


um automatizador


/home/daniellima/devops/projetos/plone6/plone6-cerrado/frontend/cypress

este é o volto

/plone6-cerrado/frontend/omelette

make clean para atualizar o projeto


backend do proprio volto

/home/daniellima/devops/projetos/plone6/plone6-cerrado/frontend/omelette/src/express-middleware

plugin

desenvolver sempre plugin

para instalar yarn add -w caminho do meu pacote

(ele sera inserido no package,json como dependecis)

depois faer manualmente no addons do package,jsno





postgresql:
  image: postgres:9.6
  ports:
    - "127.0.0.1:5432:5432"
  environment:
    POSTGRES_DB: "guillotina"
    POSTGRES_USER: "postgres"
  volumes:
    - ./postgres-data:/var/lib/postgresql/data