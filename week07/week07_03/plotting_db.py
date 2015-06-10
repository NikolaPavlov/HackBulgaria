from histogram import Histogram
import matplotlib.pyplot as plt
import sqlite3


servers = {
    "apache": "%Apache%",
    "nginx": "%nginx%",
    "iis": "%IIS%",
    "lighttpd": "%lighttpd%",
    "Failed": "%FAILED%"
}
h = Histogram()


db = sqlite3.connect('DBs/domains.db')
cursor = db.cursor()

for server in servers:
    count_row = cursor.execute('''SELECT COUNT(*) FROM domains_srv WHERE Server LIKE ? ''', (servers[server], ))
    count = count_row.fetchone()
    h.add(server, count[0])

count_row = cursor.execute('''SELECT COUNT(*) FROM domains_srv WHERE
 Server not LIKE ?
 AND Server not LIKE ?
 AND Server not LIKE ?
 AND Server not LIKE ?
 AND Server not LIKE ?
 AND Server is  not null''',
                           (servers['apache'], servers['nginx'], servers['iis'], servers['lighttpd'], servers['Failed']))
count = count_row.fetchone()
h.add('Others', count[0])

h = h.get_dict()
print(h)

keys = list(h.keys())
values = list(h.values())

X = list(range(len(keys)))

plt.bar(X, list(h.values()), align="center")
plt.xticks(X, keys)

plt.title("Crawled domains")
plt.xlabel(h)
plt.ylabel("Count")

plt.savefig("histogram.png")
