import unittest
from StartBgCrawling import CrawlStartBg


class TestCrawlStartBG(unittest.TestCase):

    def test_collecting_catalogs(self):
        #startbg_catalogs = CrawlStartBg()
        #startbg_catalogs.find_catalogs()
        #for catalog in startbg_catalogs.catalogs:
            #print (catalog)

        #for f in startbg_catalogs.sub_catalogs:
            #print (f)
        pass

    def test_collecting_sub_catalogs(self):
        #startbg_catalogs = CrawlStartBg()
        #startbg_catalogs.find_catalogs()
        #startbg_catalogs.find_sub_catalogs()
        #startbg_catalogs.find_domains_in_scatalogs()
        #startbg_catalogs.save_all()
        pass

    def test_load_all(self):
        load_info = CrawlStartBg()
        load_info.load_all()
        print(len(load_info.ext_sites))
        for site in load_info.ext_sites:
            print (site)


if __name__ == '__main__':
    unittest.main()
