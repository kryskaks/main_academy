from peewee import Model, SqliteDatabase, CharField, DateTimeField, DoubleField

db = SqliteDatabase("payments.db")


class Payment(Model):
    class Meta:
        database = db
        db_table = "payments"

    name = CharField()
    created = DateTimeField()
    amount = DoubleField()
    currency = CharField()

    def __str__(self):
        return f"Payment (id={self.id}) of {self.name}: {self.amount} {self.currency}"

    @staticmethod
    def print_all(payments):
        return [str(p) for p in payments]

    def to_str(self):
        return str(self)
