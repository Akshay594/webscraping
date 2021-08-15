import scrapy


class SmartphoneSpider(scrapy.Spider):
    name = 'smartphone'
    start_urls = [
        "https://www.amazon.in/s?k=smartphones&rh=n%3A1805560031&ref=nb_sb_noss"
    ]

    def parse(self, response):
        title = response.css('.a-color-base.a-text-normal::text').extract()
        # price = response.css('._1_WHN1::text').extract()
        # description = response.css('.rgWa7D::text').extract()

        yield {
            'title': title}
        #     'price': price,
        #     'description': description,
        # }
