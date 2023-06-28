import requests

#acessando com usuário e senha
session = requests.Session()
session.auth = ('admin', 'admin')
session.headers.update({'Accept': 'application/json'})

response = session.get('http://localhost:8080/Plone')

print('resposta do acesso: ', response)

#geranbdo token
response = requests.post('http://localhost:8080/Plone/@login', headers={'Accept': 'application/json', 'Content-Type': 'application/json'}, json={'login': 'admin', 'password': 'admin'})

response_json = response.json()

print('token obtido', response_json.get('token'))

#autenticando com token
response = requests.get('http://localhost:8080/Plone/', headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + response_json.get('token')})

print('resposta do acesso com token: ', response)

#renovar o token
response = requests.post('http://localhost:8080/Plone/@login-renew', headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + response_json.get('token')})

response_json = response.json()

print('token renovado', response_json.get('token'))

# logout (status 204 esperado)

response = requests.post('http://localhost:8080/Plone/@logout', headers={'Accept': 'application/json', 'Authorization': 'Bearer ' + response_json.get('token')})

print('resposta do logout: ', response)