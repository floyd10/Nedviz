from Driver import Bot
from datetime import datetime
from multiprocessing import Pool

# urls_xpath = '//a[contains(@href,"sale/flat") and text() ="Подробнее"]'


class Cian(Bot):
    base_url = f'https://ekb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=50&region=4743'

    def link_grabber(self):
        try:
            cian = Cian()
            cian.start()
            cian.find_links()
            cian.end()
        except Exception as e:
            print('упало')
            print(e)
            cian.end()

    def link_opener(self):
        self.open_links()

    def main(self):
        self.link_grabber()

        with Pool(40) as p:
            p.map(self.link_grabber(), self.links)

main()
