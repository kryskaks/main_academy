import datetime
import itertools


class Person:
    current_bdate = datetime.datetime(1970, 1, 1)
    all_persons = {}

    def __init__(self, name, bdate):
        self._name = name
        self._bdate = bdate
        Person.all_persons[name] = self
        # print(f"created new person {self}")

    @classmethod
    def exists(cls, name):
        return name in cls.all_persons

    def __str__(self):
        return f"{self.__class__.__name__} with name {self._name} and birthdate {self._bdate}"

    @classmethod
    def create_from_line(cls, line):
        # Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;
        name, *_ = line.split(";")
        return cls.get_or_create_with_name(name)

    @classmethod
    def get_or_create_with_name(cls, name):
        if cls.exists(name):
            # print(f"got existing one with name {name}")
            return cls.all_persons[name]
        cls.current_bdate += datetime.timedelta(days=50)
        return cls(name, Person.current_bdate)

    @classmethod
    def create_random(cls):
        random_name = "Name"
        random_date = Person.current_bdate
        return cls(random_name, random_date)

    def print(self, **kwargs):
        print(self, **kwargs)

    def sort_persons_by_name(persons):
        return sorted(persons, key=lambda p: p._name)

    @staticmethod
    def print_persons(persons):
        [p.print(end="****") for p in persons]

    def __eq__(self, other):
        print("in __eq__")
        return isinstance(other, Person) and self._name == other._name and self._bdate == other._bdate

    def __hash__(self):
        return hash(self._name)


class Payer(Person):
    def __init__(self, name, bdate):
        super().__init__(name, bdate)
        self._payments = []

    def add_payment(self, payment):
        self._payments.append(payment)


class Payment:
    current_id = 1

    def __init__(self, amount, currency, date, payer):
        self._amount = amount
        self._currency = currency
        self._date = date
        self._payer = payer
        self._id = Payment.current_id

        self._payer.add_payment(self)

        Payment.current_id += 1

    def __str__(self):
        return f"Payment(id={self._id}) of payer {self._payer}"

    @classmethod
    def create_from_line(cls, line):
        # Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;
        name, amount_and_currency, date, *_ = line.split(";")
        amount, currency = amount_and_currency.split()
        amount = float(amount.replace(",", "."))
        payer = Payer.get_or_create_with_name(name)
        return cls(amount, currency, date, payer)

    @staticmethod
    def sort_by_currency(payment):
        return payment._currency


p1 = Payer.create_from_line("Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;")
p2 = Person.create_from_line("Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;")
p3 = Payer.create_from_line("Kate Lupin;329.76 EUR;2018-08-20 19:36:32;out;")

# setattr(p1, attr_name, attr_value)

with open("2018-08-20.txt") as f:
    paymetns = [Payment.create_from_line(line) for line in f if "out" in line]

# print(paymetns[0]._payer._payments[0]._new)
# print(paymetns[0].new_attr)

# [print(p) for p in paymetns]
gen = ((p._amount, p._currency) for p in paymetns)
print(gen)
gen_usd = (amount for amount, currency in gen if currency == "USD")
print(gen_usd)
print(round(sum(gen_usd), 2))
gen = (p._amount for p in paymetns)
print(round(sum(gen), 2))

paymetns.sort(key=Payment.sort_by_currency)

# [print(p) for p in paymetns]
print(len(paymetns))

grouped_by_currency = {}
for key, group in itertools.groupby(paymetns, key=Payment.sort_by_currency):
    grouped_by_currency[key] = list(group)

# print(grouped_by_currency)

for currency in grouped_by_currency:
    print(f"Total amount in {currency}:")
    print(sum((p._amount for p in grouped_by_currency[currency])))


# p1.print()  # Person.print(p1)
# p2.print()

# p3 = p1.create_from_line("Kate Blanshet;329.76 EUR;")
# p3.print()

# sorted_persons = Person.sort_persons_by_name([p1, p2, p3])
# print("sorted by name")
# print(sorted_persons)
# [p.print() for p in sorted_persons]
