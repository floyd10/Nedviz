import concurrent
import multiprocessing
from queue import Queue
from Driver import Bot
from multiprocessing import Pool, Manager, Process
# urls_xpath = '//a[contains(@href,"sale/flat") and text() ="Подробнее"]'
import os
from functools import partial
from concurrent.futures import ProcessPoolExecutor
import threading
import random
from joblib import Parallel, delayed


class Cian(Bot):
    base_url = f'https://ekb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=45&region=4743'


def data_grabber(link):
    cian = Cian()
    cian.start()
    cian.open_links(link)


def link_collector(cian):
    try:
        links = cian.find_links()
    except Exception as e:
        print('упало')
        print(e)
    finally:
        cian.end()


def returner(cian):
    cian.returner()

def main(args):
    cian = Cian()

    cian.returner()


if __name__ == '__main__':
    cian = Cian()
    returner(cian)



#  futures = []
#  with ProcessPoolExecutor(max_workers=2) as executor:
#      while not links.empty():
#          link = executor.submit(link_collector())
#          print(f"Got link: {link}")
#          result = executor.submit(data_grabber, link)
#          futures.append(result)
#
#  for future in as_completed(futures):
#      print(future)
