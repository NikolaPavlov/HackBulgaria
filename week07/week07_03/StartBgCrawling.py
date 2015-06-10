import requests
from bs4 import BeautifulSoup
import re
import pickle


class CrawlStartBg:

    ISLINK = re.compile(r'^(http|https)://')
    ISCATALOG = r'^(http|https)://katalog.start.bg/%'
    ISSTARTBG = ('start.bg', 'start.bg/')
    ISREDIRECTLINK = r'^link.php[?]id='

    def __init__(self):
        self.ext_sites = set()
        self.catalogs = set()
        self.sub_catalogs = set()

    def find_catalogs(self):
        source_html = requests.get("http://www.start.bg/")
        soup_html = BeautifulSoup(source_html.text)
        self.sub_catalogs.add('http://register.start.bg/')

        for link in soup_html.find_all('a'):
            c_url = str(link.get('href'))
            if re.match(CrawlStartBg.ISCATALOG, c_url):
                self.catalogs.add(c_url)
            elif CrawlStartBg.ISLINK.match(c_url) and c_url.endswith(CrawlStartBg.ISSTARTBG):
                self.sub_catalogs.add(c_url)

    def find_sub_catalogs(self):
        for sub_cat in self.catalogs:
            sub_cat_html = requests.get(sub_cat)
            soup_2html = BeautifulSoup(sub_cat_html.text)
            for link in soup_2html.find_all('a'):
                sc_url = str(link.get('href'))
                if CrawlStartBg.ISLINK.match(sc_url) and sc_url.endswith(CrawlStartBg.ISSTARTBG):
                    self.sub_catalogs.add(sc_url)

    def find_domains_in_scatalogs(self):
        for scatalog in self.sub_catalogs:
            sc_html = requests.get(scatalog)
            soup_3html = BeautifulSoup(sc_html.text)
            for link in soup_3html.find_all('a'):
                redirect_link = str(link.get('href'))
                if re.match(CrawlStartBg.ISREDIRECTLINK, redirect_link):
                    redirect_url = scatalog + redirect_link
                    try:
                        rdr_head = requests.head(redirect_url, timeout=1.5)
                        domain_url = (rdr_head.headers['location'])
                        if CrawlStartBg.ISLINK.match(domain_url):
                            norm_durl = ('/'.join(domain_url.split('/')[:3]))
                            self.ext_sites.add(norm_durl)
                    except:
                        pass

    def save_all(self):
        with open('catalogs.bin', 'wb') as cf:
            pickle.dump(self.catalogs, cf)

        with open('sub_catalogs.bin', 'wb') as scf:
            pickle.dump(self.sub_catalogs, scf)

        with open('ext_sites.bin', 'wb') as domainf:
            pickle.dump(self.ext_sites, domainf)

    def load_all(self):

        with open('catalogs.bin', 'rb') as cf:
            self.catalogs = pickle.load(cf)

        with open('sub_catalogs.bin', 'rb') as scf:
            self.sub_catalogs = pickle.load(scf)

        with open('ext_sites.bin', 'rb') as domainf:
            self.ext_sites = pickle.load(domainf)
