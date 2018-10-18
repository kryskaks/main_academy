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


def init_db():
    XRate.drop_table()
    XRate.create_table()

    XRate.create(from_currency="USD", to_currency="UAH", rate=1.0)

    print("db created!")
