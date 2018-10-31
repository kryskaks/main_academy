
import requests

from models import XRate
from utils import create_logger


def get_rates_from_db():
    # update_from_privat_api()
    return [{"from_currency": rate.from_currency,
             "to_currency": rate.to_currency,
             "rate": rate.rate} for rate in XRate.select()]


def update_from_privat_api():
    log = create_logger("MainLog", "main.log")
    log.info("Started update rate via privatbank api")

    response = get_rates_from_privat()
    # response = PrivatApi().get_rates()

    log.debug(f"response: {response}")

    check_response(response)
    rates = [(rate_info["ccy"], rate_info["base_ccy"], float(rate_info["sale"])) for rate_info in response]

    log.debug(f"rates: {rates}")

    for from_currency, to_currency, rate in rates:
        db_rate = XRate.select().where(XRate.from_currency == from_currency,
                                       XRate.to_currency == to_currency).first()

        if not db_rate:
            db_rate = XRate(from_currency=from_currency, to_currency=to_currency)
            log.debug(f"{db_rate} was created")

        db_rate.rate = rate
        db_rate.save()

    log.info("Finished update rate via privatbank api")


def get_rates_from_privat():
    response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11", timeout=2)
    response.status_code
    json_resp = response.json()

    return json_resp


class ResponseException(Exception):
    pass


def check_response(response):
    for rate_info in response:
        for attr in ("ccy", "base_ccy", "sale"):
            if attr not in rate_info:
                raise ResponseException(f"{attr} is not set")


class PrivatApi:

    def get_rates(self):
        return requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11").json()
