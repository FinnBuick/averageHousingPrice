import scrapy


class PricesSpider(scrapy.Spider):
	name = "prices"

	start_urls = [
		"https://www.realestate.com.au/sold/in-manly%2c+nsw+2095%3b/list-1",
	]

	def parse(self, response):
		for price in response.css("div.property-card__content"):
			yield {
				'price': price.css("span.property-price::text").extract_first()
			}

		next_page = response.css('div.pagination__next a::attr(href)').extract_first()
		if next_page is not None:
			next_page = response.urljoin(next_page)
			yield scrapy.Request(next_page, callback=self.parse)