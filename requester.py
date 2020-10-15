import requests
import json
r = requests.post('http://127.0.0.1:8000/signup',
              json.dumps({'user_id': '0',
               'user_name': 'username',
               'password': '123'}))

print(r.text)

r = requests.post('http://127.0.0.1:8000/login',
              json.dumps({'user_id': '0',
               'user_name': 'username',
               'password': '123'}))

print(r.text)
