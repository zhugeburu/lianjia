import scrapy
from lianjia.items import lianjiaItem

class lianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ["lianjia.com"]
    city_and_page = {
            'dongcheng': 99, 'cicheng': 100, 'chaoyang': 100, 'haidian': 100,
            'fengtai': 100, 'shijingshan': 96, 'tongzhou': 93, 'changping': 100,
            'daxing': 100, 'yizhuangkaifaqu': 52, 'shunyi': 100, 'fangshan': 100, 
            'mentougou': 49, 'pinggu': 0, 'huairou': 1, 'miyun': 1, 'yanqing': 1,
            'yanjiao': 100}
    start_urls = []
    for i in range(100):
        start_urls.append("http://bj.lianjia.com/ershoufang/xicheng/pg%s/" % str(i+1))

    def parse(self, response):
        if response.status == 200:
            lianjia = lianjiaItem()
            lianjia['price_of_house'] = response.xpath('/html/body/div[4]/div[1]/ul/li[1]/div[1]/div[1]/a/text()').extract_first()
            print repr(lianjia).decode("unicode-escape") + '\n'
            yield lianjia
            # for sel in response.xpath("//div[@class='listContent']"):
            #     lianjia = lianjiaItem()
            #     lianjia['name_of_community'] = sel.css("div.title a::text").extract_first()
            #     # lianjia['layout_of_house'] = sel.xpath("div[1]/div[1]/span[1]/span/text()").extract_first()
            #     # lianjia['price_of_house'] = sel.xpath("div[2]/div[1]/span/text()").extract_first()
            #     # lianjia['area_of_house'] = sel.xpath("div[1]/div[1]/span[2]/text()").extract_first()
            #     # lianjia['time_of_construction'] = sel.xpath("div[1]/div[2]/div/text()").extract_first()
            #     print repr(lianjia).decode("unicode-escape") + '\n'
            #     yield lianjia
