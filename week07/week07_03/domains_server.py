import requests
import pickle
import sqlite3


class CollectingServersSQL:

    def __init__(self):
        self.domains = set()
        self.db = sqlite3.connect('DBs/domains.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS
            domains_srv(id INTEGER PRIMARY KEY,
                domain TEXT UNIQUE,
                Server TEXT)
        ''')
        self.db.commit()
        self.db.close()

    def loading_domains(self):
        with open('ext_sites.bin', 'rb') as domainfile:
            self.domains = pickle.load(domainfile)

    def populating_domains(self):
        self.db = sqlite3.connect('DBs/domains.db')
        self.cursor = self.db.cursor()

        for domain in self.domains:
            self.cursor.execute('''
                INSERT INTO domains_srv(domain)
                VALUES(?)
                ''', (domain, )
            )

        self.db.commit()
        self.db.close()

    def populate_domain_servers(self):
        self.db = sqlite3.connect('DBs/domains.db')
        self.cursor = self.db.cursor()
        self.cursor.execute('''SELECT * FROM domains_srv WHERE Server is null''')
        domainsdb = self.cursor.fetchall()

        our_headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36"
        }

        for row in domainsdb:
            try:
                rq_head = requests.head(row[1], timeout=3, headers=our_headers, allow_redirects=True)
                srv = (rq_head.headers['Server'])
                self.cursor.execute('''UPDATE domains_srv SET Server = ? WHERE id = ?''', (srv, row[0]))

            except Exception as e:
                self.cursor.execute('''UPDATE domains_srv SET Server = ? WHERE id = ?''', ('FAILED', row[0]))
                print(e)

            self.db.commit()

        self.db.close()


def main():

    srvdb = CollectingServersSQL()
    srvdb.populate_domain_servers()


if __name__ == '__main__':
    main()
