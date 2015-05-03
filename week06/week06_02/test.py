import requests

# r = requests.get('https://api.github.com/users/radorado?client_id=...&client_secret=...')
r = requests.get('https://api.github.com/users/radorado?client_id=61dec489551058e407cf&client_secret=2cdced69d2f35611f77b66a69f061bb658f55c19')
# resources /../../../../
# params /../../../../?key=value
#print(r.json())
workable_json = json.dump(r, )
#print(r.headers)

# library for parsin HTML python ?
