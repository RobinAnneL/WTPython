print('Start api uitless applicatie')

import requests

paginaresults = requests.get('https://catfact.ninja/facts')
print (paginaresults)

feitjes = paginaresults.json()
print("Feitje is "+ feitjes["data"][0]["fact"])
