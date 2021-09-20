import scrapy
from scrapy.crawler import CrawlerProcess
from datetime import datetime


now = datetime.now()
currentTime = now.strftime("%H:%M:%S")

data = open('data1.csv', 'a')

classLinks = open('classLinks.csv', 'r')
lists = classLinks.readlines()[0].split(',')
linkList =[]
for i in range(len(lists)-1):
    classLinks.seek(0)
    lists = classLinks.readlines()[0].split(',')[i]
    linkList.append(lists)

classLinks.close()

class ClassSpider(scrapy.Spider):
    name = 'spider'

    # urls we will be extracting from
    start_urls = linkList
    # crnNum = (start_urls[0].split('=')[2])

    # items we will be getting
    def parse(self, response):
        crn = response.request.url.split('=')[2]
        max = (str(response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "dddefault", '
                                  '" " ))]//*[contains(concat( " ", @class, " " ), concat( " ", '
                                  '"dddefault", '
                                  '" " ))]').extract()).split('>')[1]).split('<')[0]
        avl = (str(response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "dddefault", '
                                  '" " ))]//*[contains(concat( " ", @class, " " ), concat( " ", '
                                  '"dddefault", '
                                  '" " ))]').extract()).split('>')[5]).split('<')[0]
        if int(currentTime.split(':')[2]) % 5 == 0:
            data.write(crn + "," + avl + "," + max + "," + currentTime + '\n')
        return max


process = CrawlerProcess()
process.crawl(ClassSpider)
process.start()
