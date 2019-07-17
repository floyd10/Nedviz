import time
from threading import Thread
from Driver import Bot
from datetime import datetime
from concurrent.futures import ProcessPoolExecutor
# urls_xpath = '//a[contains(@href,"sale/flat") and text() ="Подробнее"]'
from multiprocessing import Process, Queue, current_process
from functools import partial
import asyncio
from os import getpid



def test(num):
    print(f"Get link: {num} in {getpid()}")
    time.sleep(1)
    print("End")

class Cian(Bot):

    base_url = f'https://ekb.cian.ru/cat.php?deal_type=sale&engine_version=2&offer_type=flat&p=52&region=4743'


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=10) as executor:
        try:
            cian = Cian()
            cian.start()
            links = cian.find_links()
        except Exception as e:
            print('упало')
            print(e)
            cian.end()
        finally:
            cian.end()
        result = executor.map(cian.open_links, links)

    # results = Queue()
    # pr = []
    # num_workers = 4
    # for i in range(num_workers):
    #     process = Process(target=cian.open_links)
    #     process.start()
    #     pr.append(process)
    #
    # while num_workers:
    #     item = results.get()
    #     if item is None:
    #         num_workers -= 1
    # for process in pr:
    #     process.join()

  #  pool = ThreadPool(10)
  #  pool.map(Thread.start, [Thread(target=cian.open_links(), args=(x,)) for x in range(10)])
  #  pool.close()
  #  pool.join()

