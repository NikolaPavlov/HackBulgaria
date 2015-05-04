import requests
from requests.auth import HTTPBasicAuth

# test git hub with basic auth ( it's worked!!!)
# print(requests.get('https://api.github.com/user', auth=HTTPBasicAuth('NikolaPavlov', 'secret-pass')))

# test mail.bg with basic auth
# print(requests.get('http://mail.bg', auth=HTTPBasicAuth('rastamandito@mail.bg', 'secret-pass')).status_code)
# print(requests.get('http://mail.bg', auth=HTTPBasicAuth('rastamandito@mail.bg', 'secret-pass')).content)
# print(requests.get('http://mail.bg', auth=HTTPBasicAuth('rastamandito@mail.bg', 'secret-pass')).headers)
# print(requests.get('http://mail.bg', auth=HTTPBasicAuth('rastamandito@mail.bg', 'secret-pass')))





'''
{'server': 'nginx/1.6.2', 'connection': 'keep-alive', 'expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'pragma': 'no-cache', 'content-type': 'text/html; charset=utf-8', 'x-frame-options': 'SAMEORIGIN', 'date': 'Wed, 22 Apr 2015 17:58:22 GMT', 'set-cookie': 't=l.bg; expires=Thu, 21-Apr-2016 17:58:22 GMT; path=/; domain=.mail.bg, s=dab02cbb5749e8714a8f19b7b3d5be5b; path=/; domain=mail.bg; HttpOnly, t=f; expires=Thu, 21-Apr-2016 17:58:22 GMT; path=/; domain=.mail.bg, OAID=d69c891ba2f3af2405ddf6507856098b; expires=Thu, 21-Apr-2016 17:58:22 GMT; path=/; domain=.mail.bg, OAID=d69c891ba2f3af2405ddf6507856098b; expires=Thu, 21-Apr-2016 17:58:22 GMT; path=/; domain=.mail.bg', 'vary': 'Accept-Encoding', 'cache-control': 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0', 'transfer-encoding': 'chunked', 'content-encoding': 'gzip', 'p3p': 'CP="CUR ADM OUR NOR STA NID"'}
'''
