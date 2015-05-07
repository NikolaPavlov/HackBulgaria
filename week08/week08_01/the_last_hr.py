import requests
import sqlite3


HEADERS = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}


class Crawler:

    def __init__(self, url):
        r = requests.get(url, headers=HEADERS)
        self.data = r.json()
        self.users = []

    def set_users(self):
        for line in self.data:
            name = line['name']
            github = line['github']
            courses = line['courses']
            self.users.append(line['name'], line['github'], line['courses'])

    def get_data(self):
        print(self.data)


cw = Crawler('https://hackbulgaria.com/api/students/')
# cw.get_data()
print(cw.users())
