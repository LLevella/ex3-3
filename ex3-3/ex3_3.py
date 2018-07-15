import requests
import urllib
import json

APP_ID = '6633040'
AUTH_SERVER = 'https://oauth.vk.com/authorize'
TOKEN = 'cdfb7ea64b545a71a2cfea657aac9112e7d2223869bf5e7b9b0a01c6f3cf4d570ed0f58ca46b2e2f73aaa'
auth_data = {
    'client_id': APP_ID,
    'display': 'popup',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.80'
    }
print('?'.join((AUTH_SERVER, urllib.parse.urlencode(auth_data))))


FRIENDS_SERVER = 'https://api.vk.com/method/friends.get'
friends_get_params = {
    'access_token': TOKEN,
    'v': '5.80',
    'order': 'name',
    'fields': 'city'
    }
requests_for_friends = requests.get(FRIENDS_SERVER, params=friends_get_params)
print(requests_for_friends.json())
dict_friends_from_request = requests_for_friends.json()