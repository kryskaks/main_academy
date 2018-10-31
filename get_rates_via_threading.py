# -*- coding: utf-8 -*-
import threading
import time

import requests
import xmltodict


def main():
    privat_resp = {}
    cbr_resp = {}
    t1 = threading.Thread(target=get_rate_from_privat, args=(privat_resp, ))
    t2 = threading.Thread(target=get_rate_from_cbr, args=(cbr_resp, ))

    t1.start()
    t2.start()

    # заставляет основной поток ожидать завершения выполнения t1 и t2 потоков
    # можно проверить, как будет без них, закомментировать, сравнить
    t1.join()
    t2.join()

    print("All threads finished")
    print("privat_resp", privat_resp)
    print("cbr_resp", cbr_resp)


def get_rate_from_privat(result):
    print("in get_rate_from_privat")
    json_resp = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11").json()

    result["rate"] = json_resp[0]["sale"]
    time.sleep(10)
    print("get_rate_from_privat finished")


def get_rate_from_cbr(result):
    print("in get_rate_from_cbr")
    resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text

    time.sleep(3)
    parsed = xmltodict.parse(resp)

    result["rate"] = parsed["ValCurs"]["Valute"][0]["Value"]

    print("get_rate_from_cbr finished")


if __name__ == '__main__':
    main()
