import requests
from peewee import SqliteDatabase, Model, DoubleField, CharField

db = SqliteDatabase('xrates.db')


class XRate(Model):
    class Meta:
        database = db
        db_table = "xrates"

    from_currency = CharField()
    to_currency = CharField()
    rate = DoubleField()

    def __str__(self):
        return f"Rate {self.from_currency} => {self.to_currency}: {self.rate}"


XRate.drop_table()
XRate.create_table()


def main():
    # получить данный от апи в нужном виде - (from, to, rate)
    rate_info = get_api_rates()
    print(rate_info)

    # создание в БД
    for from_currency, to_currency, rate in rate_info:
        XRate.create(from_currency=from_currency,
                     to_currency=to_currency,
                     rate=rate)

    rates = XRate.select()
    for r in rates:
        print(r)


def get_api_rates():

    response = requests.get("https://api.privatbank.ua/p24api/pubinfo?exchange&json&coursid=11")

    json_resp = response.json()

    result = [(rate_info["ccy"], rate_info["base_ccy"], rate_info["sale"])
              for rate_info in json_resp]

    return result


main()
