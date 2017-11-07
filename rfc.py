"""
A simple module to download and print rfc document texts over http.

Usage -> python3 rfc.py {rfc_number} | less
"""

import sys, urllib.request

try:
    rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
    print ("Expect an RFC number as argument. None given.")
    sys.exit(2)

template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)

url2 = 'http://192.0.2.1/index.html'
try:
    rfc_raw = urllib.request.urlopen(url2).read()
    rfc = rfc_raw.decode()
    print (rfc)
except urllib.error.HTTPError as e:
    print ('status: ', e.code)
    print ('reason: ', e.reason)
    print ('url', e.url)
except urllib.error.URLError as ue:
    print (ue)
