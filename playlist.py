import sys
import os
import requests
import json

# The Bearer token needs to be replaced, see the README. Note that it expires after some minutes (30min?)

filepath = sys.argv[1]

headers = {'Accept': 'application/json', 'Content-Type': 'application/json', 'Authorization': 'Bearer BQCvqVpDlTCgW-mRVF
RBmsmDWwMVYVmyWO_rAFbTkM4XPPuPzOHsV_sQUsRCPpGhzs8_yBaK3nBGx8SEbkZpYotPUQmflBSceObUeadx1WKA-xC_dzr9o24vGdAfDw7gJ1L2qC-EAO
D7BYv46TqZJdVbzy5g6bui0zH2KByW-QBgcZ6dvvJ6ZFVSoQlDw5uJVyPA8xCWZWEa44piNpiWd_u2-w'}

params = ( ('type', 'track'), ('market', 'IS'), ('limit', '1'))

with open(filepath) as fp:
    for line in fp:
        params_new = (('q', line.strip()),) +  params

        response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=params_new)
        data = response.json()

        uri = data['tracks']['items'][0]['uri']
        print(uri, end=',')
