import requests
import urllib
import json
import pprint

APP_ID = '6633040'
AUTH_SERVER = 'https://oauth.vk.com/authorize'
FRIENDS_SERVER = 'https://api.vk.com/method/friends.get'
TOKEN = 'cdfb7ea64b545a71a2cfea657aac9112e7d2223869bf5e7b9b0a01c6f3cf4d570ed0f58ca46b2e2f73aaa'

def create_straddres_for_token_extraction():
    auth_data = {
        'client_id': APP_ID,
        'display': 'popup',
        'redirect_uri': 'https://oauth.vk.com/blank.html',
        'scope': 'friends',
        'response_type': 'token',
        'v': '5.80'
        }
    return '?'.join((AUTH_SERVER, urllib.parse.urlencode(auth_data)))

def get_friends_from_get_request():
    friends_get_params = {
        'access_token': TOKEN,
        'v': '5.80',
        'order': 'name',
        'fields': 'city'
        }
    requests_for_friends = requests.get(FRIENDS_SERVER, params=friends_get_params)
    pprint.pprint(requests_for_friends.json())
    dict_friends_from_request = requests_for_friends.json()
    return dict_friends_from_request

def error_handler(dict_friends_from_request):
    if 'error' in dict_friends_from_request:
        print(dict_friends_from_request['error']['error_msg'])
        print('Пройдите по адресу для получения токена: {}'.format(create_straddres_for_token_extraction()))
        return True
    return False

def output_list_of_friends(dict_friends_from_request):
    if dict_friends_from_request['response']:
        print ("Друзей найдено: {}".format(dict_friends_from_request['response']['count']))
    
        for item in dict_friends_from_request['response']['items']:
            first_name = 'Имя не указано'
            if 'first_name' in item:
                first_name = item['first_name']
            last_name = 'Фамилия не указана'
            if 'last_name' in item:
                last_name = item['last_name']
            city = 'Город не указан'
            if 'city' in item:
                if item['city']['title']:
                    city = item['city']['title']
            print('{} {} {}'.format(first_name, last_name, city))


dict_friends_from_request = get_friends_from_get_request()
error_handler(dict_friends_from_request)
output_list_of_friends(dict_friends_from_request)