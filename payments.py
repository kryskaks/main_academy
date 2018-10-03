import datetime


class Person:
    current_bdate = datetime.datetime(1970, 1, 1)

    def __init__(self, name, bdate):
        self._name = name
        self._bdate = bdate

    def __str__(self):
        return f"{self.__class__.__name__} with name {self._name} and birthdate {self._bdate}"

    @classmethod
    def create_from_line(cls, line):
        # Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;
        print(cls)
        name, *_ = line.split(";")
        Person.current_bdate += datetime.timedelta(days=50)
        return cls(name, Person.current_bdate)

    @classmethod
    def create_random(cls):
        random_name = "Name"
        random_date = Person.current_bdate
        return cls(random_name, random_date)

    def print(self, **kwargs):
        print(self, **kwargs)

    @staticmethod
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

    def __add__(self, other):
        if not isinstance(other, Person):
            raise ValueError()
        return self


class Payer(Person):
    def __init__(self, name, bdate):
        super().__init__(name, bdate)
        self._payments = []

    def add_payment(self, payment):
        self._payments.append(payment)

    def __add__(self, other):
        if not isinstance(other, Payer):
            raise ValueError("Not Payer!!")
        return self


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
        return f"Payment(id={self._id})"


p1 = Person.create_random()
p2 = Payer.create_random()
p3 = Payer.create_from_line("Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;")

pmt = Payment(10, "UAH", datetime.datetime.now(), p3)
pmt2 = Payment(100, "UAH", datetime.datetime.now(), p3)
print(pmt, pmt2)

print(p3._payments)

# p1 = Person.create_from_line("Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;")
# p2 = Payer.create_from_line("Kate Lupin;329.76 EUR;2018-08-20 19:36:32;out;")

# p1.print()  # Person.print(p1)
# p2.print()

# p3 = p1.create_from_line("Kate Blanshet;329.76 EUR;")
# p3.print()

# sorted_persons = Person.sort_persons_by_name([p1, p2, p3])
# print("sorted by name")
# print(sorted_persons)
# [p.print() for p in sorted_persons]
