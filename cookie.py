""" A simple cookie handling program. """

# http.cookiejar also provides
# FileCookieJar class, which is
# same as CookieJar but persistent.

from http.cookiejar import CookieJar
cookie_jar = CookieJar()

# urllib opener to extract the cookies
# from the response and store in our cookie jar.
from urllib.request import build_opener, HTTPCookieProcessor
opener = build_opener(HTTPCookieProcessor(cookie_jar))

# then we use opener to make
# the http request
opener.open('http://www.github.com')

print (len(cookie_jar))

cookies = list(cookie_jar)
print (cookies)
# further requests using opener will
# make HTTPCookieProcessor to check
# our cookie jar and will add them
# to our requests.
