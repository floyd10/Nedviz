from Driver import Bot

#urls_xpath = '//a[contains(@href,"sale/flat") and text() ="Подробнее"]'


class Cian(Bot):

    base_url = f'https://ekb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=4743'


if __name__ == '__main__':
    cian = Cian()
    cian.start()
    cian.find_links()
    cian.end()
