from Driver import Bot

#urls_xpath = '//a[contains(@href,"sale/flat") and text() ="Подробнее"]'


class Cian(Bot):

    base_url = f'https://ekb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=1&region=4743'


if __name__ == '__main__':
    cian = Cian()
    cian.start()

#-----
    cian.find_links(


    # def get_links(self, html):
    #     html_parsed = ht.fromstring(html.text)
    #     links = html_parsed.xpath(urls_xpath)
    #     links_parsed = [x.get('href') for x in links]
    #     return links_parsed
    #
    # def next_page(self, url):
    #     pass
    #
    # def get_flat_attribute(self, url):
    #     main_info_title_xpath = '//div[@itemscope and @class[contains(.,"info")]]/div'
    #     html = req.get_html(self, url)
    #     html_parsed = ht.fromstring(html.text)
    #     print(html.text)
    #     main_info_blocks = html_parsed.xpath(main_info_title_xpath)
    #     print([x.get('class') for x in main_info_blocks])
    #    #     main_info_blocks.append(x.get('Text'))
    #    # print(main_info_blocks)
    #
    #     #main_info_data = [x.get('class') for x in main_info_blocks]
    #     #print(main_info_data)
