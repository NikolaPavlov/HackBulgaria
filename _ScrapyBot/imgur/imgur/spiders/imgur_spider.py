import scrapy
from scrapy.contrib.spiders import Rule, CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor
from imgur.items import ImgurItem


class ImgurSpider(CrawlSpider):
    name = 'imgur'
    allowed_domains = ['imgur.com']
    start_urls = ['http://www.imgur.com']
    rules = [Rule(LinkExtractor(allow=['/gallery/.*']), 'parse_imgur')]

    def parse_imgur(self, response):
        image = ImgurItem()
        image['title'] = response.xpath(\
                "//h2[@id='image-title']/text()").extract()
        rel = response.xpath("//img/@src").extract()
        image['image_urls'] = ['http:'+rel[0]]
        return image


