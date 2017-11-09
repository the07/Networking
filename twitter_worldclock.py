""" Implementation of the twitter api to display the time of the city mentioned in a tweet. """

import requests, requests_oauthlib, sys
import pytz
import datetime

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

def get_mentions(since_id, auth_obj):
    # TODO : Use Twitter streaming API, to prevent loss in case there are more than 200 tweets. Requests has iter_lines() which runs indefinately.
    params = {'count': 200, 'since_id': since_id, 'include_rts': 0, 'include_entities': 'false'} #include_rts - tells twitter not to include any retweets
    url = 'https://api.twitter.com/1.1/statuses/mentions_timeline.json'
    response = requests.get(url, params=params, auth=auth_obj)
    response.raise_for_status()
    return json.loads(response.text)

def process_tweet(tweet):
    username = tweet['user']['screen_name']
    text = tweet['text']
    words = [x for x in text.split() if x[0] not in ['@', '#']]
    place = ' '.join(words)
    check = place.replace(' ', '_').lower()
    found = False
    for tz in pytz.common_timezones:
        tz_low = tz.lower()
        if check in tz_low.split('/'):
            found = True
            break
        if found:
            timezone = pytz.timezone(tz)
            time = datetime.datetime.now(timezone).strftime('%H: %M')
            reply = '@{} The time in {} is currently {}'.format(username, place, time)
        else:
            reply = '@{} Sorry, I did not recognize {} as a city'.format(username, place)
        print (reply)
        post_reply(tweet['id'], reply, auth_obj)

def post_reply(reply_to_id, text, auth_obj):
    params = {
        'status': text,
        'in_reply_to_status_id': reply_to_id
    }

    url = 'https://api.twitter.com/1.1/statuses/update.json'
    response = requests.post(url, params=params, auth=auth_obj)
    response.raise_for_status()

if __name__ == '__main__':
    auth_obj = init_auth()

    since_id = 1
    error_count = 0
    while error_count < 15:
        try:
            for tweet in get_mentions(since_id, auth_obj):
                process_tweet(tweet)
                since_id = max(since_id, tweet['id'])
            error_count = 0
        except requests.exceptions.HTTPError as e:
            print ('Error: {}'.format(str(e)))
            error_count += 1
        time.sleep(60)
