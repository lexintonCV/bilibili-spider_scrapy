# -*- coding: utf-8 -*-
import scrapy
from bilibili.items import BilibiliItem


class BilibiliSpider(scrapy.Spider):
    name = 'bilibili'
    allowed_domains = ['bilibili.com']
    start_urls = ['https://www.bilibili.com/ranking/all/0/0/3']

    def parse(self, response):
        rank_list = response.xpath('..//li[@class="rank-item"]')
        print("-----")
        for rank_item in rank_list:
            item = BilibiliItem()
            item['title'] = rank_item.xpath('./div[@class="content"]/div[@class="info"]/a/text()')[0].extract()
            item['href'] = rank_item.xpath('./div[@class="content"]/div[@class="info"]/a/@href')[0].extract()
            yield item
        pass
