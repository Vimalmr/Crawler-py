import scrapy

class MySpider(scrapy.Spider):
    name = 'MySpider'
    allowed_domains = ['kongu.ac.in']
    start_urls = ['http://kongu.ac.in']

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.visited_urls = set()

    def parse(self, response):
        self.visited_urls.add(response.url)
        for link in response.css('a::attr(href)').getall():
            if link.startswith('http') and link not in self.visited_urls:
                yield scrapy.Request(link, callback=self.parse)
        
        # Return the visited URLs
        yield {
            'visited_urls': list(self.visited_urls)
        }
