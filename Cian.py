from Driver import Bot
from multiprocessing import Pool, Manager
from concurrent.futures import ProcessPoolExecutor, as_completed
# urls_xpath = '//a[contains(@href,"sale/flat") and text() ="Подробнее"]'
import os
from selenium import webdriver


class Cian(Bot):
    base_url = f'https://ekb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=53&region=4743'


def data_grabber(link):
    cian = Cian()
    cian.start()
    cian.open_links(link)


def link_collector():
    try:
        cian = Cian()
        cian.start()
        links = cian.find_links()
    except Exception as e:
        print('упало')
        print(e)
    finally:
        cian.end()
    return links


if __name__ == '__main__':



    futures = []
    with ProcessPoolExecutor(max_workers=2) as executor:
        while not links.empty():
            link = links.get()
            print(f"Got link: {link}")
            result = executor.submit(data_grabber, link)
            futures.append(result)

    for future in as_completed(futures):
        print(future)
