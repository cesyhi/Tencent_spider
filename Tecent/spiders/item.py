# -*- coding: utf-8 -*-
import scrapy
from Tecent.items import TecentItem


class ItemSpider(scrapy.Spider):
    name = 'item'
    allowed_domains = ['hr.tencent.com']
    start_urls = ['http://hr.tencent.com/position.php']
    host = "http://hr.tencent.com/"

    def parse(self, response):
        # print(response)
        node_list = response.xpath('//tr[@class="even"]|//tr[@class="odd"]')
        # print((node_list))

        # 获取所有的节点ＵＲＬ
        for node in node_list:
            item = TecentItem()
            item['name'] = node.xpath("./td[1]/a/text()").extract()[0]
            item['link'] = self.host+node.xpath("./td[1]/a/@href").extract()[0]
            item['creat'] = node.xpath("./td[2]/text()").extract_first()
            item['count'] = node.xpath("./td[3]/text()").extract()[0]
            item['address'] = node.xpath("./td[4]/text()").extract()[0]
            item['time'] = node.xpath("./td[5]/text()").extract()[0]
            # print("=================================")
            print(item)
            # print("***********************************")
            yield item

        # 翻页操作

        next_url = self.host + response.xpath('//*[@id="next"]/@href').extract()[0]
        yield scrapy.Request(next_url, callback=self.parse)