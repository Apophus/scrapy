from scrapy import Spider
from scrapy.selector import Selector
from stack.stack.items import StackItem


class StackSpider(Spider):
    # name of the spider
    name = 'stack'
    # base url for spider to crawl
    allowed_domains = ["stackoverflow.com"]
    # list of urls for spider to start crawling from
    start_urls = ["http://stackoverflow.com/questions?pages12e-50&sort=newest",
                  ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        # Extract the data
        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item
