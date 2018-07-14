import requests
import urllib

APP_ID = '6633040'
AUTH_SERVER = 'https://api.vk.com/authorize'
TOKEN = '04cdbc464ff1a0e9fc8b02684f7585927e4c6553d9aeb55293303707c97e49d2f25c620f810a3a0de0de5'
auth_data = {
    'client_id': APP_ID,
    'display': 'popup',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'scope': 'friends',
    'response_type': 'token',
    'v': '5.80'
    }

FRIENDS_SERVER = 'https://api.vk.com/method/friends.get'
friend_get_params = {
    'order': 'name',
    'fields': 'city',
    'ACCESS_TOKEN': TOKEN,
    'v': '5.80'
    }

requests_for_friends = requests.get(FRIENDS_SERVER, params=friend_get_params)
#dict_friends_from_request = json.loads(requests_for_friends.text)
print(requests_for_friends.text)