import requests
#thi will send request to website

r=requests.get("https://api.coindesk.com/v1/bpi/currentprice/USD.json")
binfo=r.json()

print(type(binfo))

print(binfo)

print(binfo['time'])
print(binfo['time']['updated'])
print(binfo['bpi']['USD']['rate'])