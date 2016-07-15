from scrapy import Spider


class StackSpider(Spider):
    name = 'stack'
    allowed_domains = ["stackoverflow.com"]
    start_urls = ["http://stackoverflow.com/questions?pages12e-50&sort=newest",]

