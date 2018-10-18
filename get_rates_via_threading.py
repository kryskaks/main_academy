import threading

import requests
import xmltodict


def main():
    privat_resp = {}
    cbr_resp = {}
    t1 = threading.Thread(target=get_rate_from_privat, args=(privat_resp, ))
    t2 = threading.Thread(target=get_rate_from_cbr, args=(cbr_resp, ))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("All threads finished")
    print("privat_resp", privat_resp)
    print("cbr_resp", cbr_resp)


def get_rate_from_privat(result):
    print("in get_rate_from_privat")
    json_resp = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11").json()

    result["rate"] = json_resp[0]["sale"]

    print("get_rate_from_privat finished")


def get_rate_from_cbr(result):
    print("in get_rate_from_cbr")
    resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp").text

    parsed = xmltodict.parse(resp)

    result["rate"] = parsed["ValCurs"]["Valute"][0]["Value"]

    print("get_rate_from_cbr finished")


if __name__ == '__main__':
    main()
