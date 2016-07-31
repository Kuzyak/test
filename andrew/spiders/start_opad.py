from scrapy.spiders import CrawlSpider, Rule
from scrapy import Selector
from scrapy.linkextractors import LinkExtractor
from andrew.items import AndrewItem
import sys

class MySpider(CrawlSpider):
    #reload(sys)
    #sys.setdefaultencoding('utf-8')
    name = "opad"
    allowed_domains = ["opad.com",
                    "olighting.com",
                    "site.olighting.com"]
    start_urls = ['http://www.opad.com/fontana-arte-fontana-coffee-table.html',
                'http://www.opad.com/moooi-random-pendant-light.html']

    '''
    rules = (
        Rule(LinkExtractor(restrict_xpaths=("//nav[@id='top-menu']//ul[@class='start2']/li/ul/li/a")), follow=True),
        Rule(LinkExtractor(restrict_xpaths=("td/ul[@class='item_grid']//div/div/a")), follow=True),
        Rule(LinkExtractor(allow=("mega.pk/[A-z0-9]+[_][a-z]+/[0-9]+/[A-z0-9-]+.html")), callback='parse_item'),
    )item = AndrewItem()
    '''

    def parse(self, response):
        hxs = Selector(response)
        items = []
        item = AndrewItem()
        item["title"] = hxs.select("//div[@class='breadcrumbs']/b/text()").extract_first()
        item["image_urls"] = hxs.select("//div[@class='scroller-view']/div/div/a/@href").extract()
        try:
            item["file_urls"] = ((hxs.select("//div[@class='ytInfoDivText']/div/a/@onclick").extract()[0]).split("('")[1]).split("','")[0]
        except:
            item["file_urls"] = ""
            print "No PDF there"
        items.append(item)
        return items
        #for url in urls:
        #    yield Request(url, self.parse_two)
