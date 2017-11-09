""" Implementation of the twitter api to display the time of the city mentioned in a tweet. """

import requests, requests_oauthlib, sys

twitter_credential_file = 'twitter.txt'

with open(twitter_credential_file) as f:
    content = f.read()

c_key, c_secret, a_token, a_secret = content.split('\n')[1].split(',')

def init_auth():
    print ('Testing credential')
    print (type(c_key))
    auth_obj = requests_oauthlib.OAuth1(c_key, c_secret, a_token, a_secret)
    if verify_credentials(auth_obj):
        print ('Validated credentials. OK')
        return auth_obj
    else:
        print ('Credentials validation failed.')
        sys.exit(1)

def verify_credentials(auth_obj):
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    response = requests.get(url, auth=auth_obj)
    print (response)
    return response.status_code == 200

if __name__ == '__main__':
    auth_obj = init_auth()
