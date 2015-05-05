# script for scanning, there is no time for Class LooseCoupling things :D
import requests
from bs4 import BeautifulSoup
from histogram import Histogram


REGISTER = "http://register.start.bg"
HEADERS = {
    "User-Agent": "User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
}


source_html = requests.get(REGISTER, headers=HEADERS).text
soup_html = BeautifulSoup(source_html)
all_valid_php_links = []
for a in soup_html.find_all('a', href=True):
    if 'link.php?id=' in a['href']:
        all_valid_php_links.append(a['href'])

visited_php_links = set()
histoG = Histogram()
answers = []
for link in all_valid_php_links:
    try:
        target_url = REGISTER + '/' + link
        r = requests.head(target_url, headers=HEADERS, allow_redirects=True, timeout=10)
        if target_url not in visited_php_links:
            visited_php_links.add(target_url)
            target_url_server = r.headers['Server']
            answers.append(target_url_server)
    except Exception as e:
        print(e)

with open('results_from_scanner.txt', 'w') as f:
    f.write('\n'.join(answers))

