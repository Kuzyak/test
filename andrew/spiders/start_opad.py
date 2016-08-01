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
                'http://www.opad.com/moooi-random-pendant-light.html',
                'http://www.opad.com/pablo-cielo-7-pendant-chandelier.html']



    def parse(self, response):
        hxs = Selector(response)
        items = []
        item = AndrewItem()
        item["file_urls"]=[]
        item["title"] = hxs.select("//div[@class='breadcrumbs']/b/text()").extract_first()
        item["image_urls"] = hxs.select("//div[@class='scroller-view']/div/div/a/@href").extract()
        try:
            z = hxs.select("//div[@class='itemPDF']/div/a/@onclick").extract()
            for i in range(len(z)):
                x = ((z[i]).split("('")[1]).split("','")[0]
                item["file_urls"].append(x)
            print item["file_urls"]
        except:
            item["file_urls"] = ""
            print "No PDF there"

        items.append(item)
        return items
        #for url in urls:
        #    yield Request(url, self.parse_two)
