# TODO интересуют только out транзакции
# TODO Полчучить список людей и сумму всех покупок в каждой валюте и кол-вом покупок
# TODO Получить список людей, которые тратили каждый день
# TODO Сформировать список людей которые тратили деньги только в первый день

import os


def take_content(path):
    # d = {key: "NAME", value: [('DATE','SPEND','CURRENCY')]}
    payments_info = {}
    files = os.listdir(path)
    for filename in files:
        if filename.endswith(".txt"):
            with open(path + "/" + filename, 'r') as file:
                lines = file.readlines()
                parse_lines(lines, payments_info)

    return payments_info


def parse_lines(lines, payments_info):
    for line in lines:
        name, amount_and_currency, date, ptype, *_ = line.split(";")
        amount, currency = amount_and_currency.split()
        amount = float(amount.replace(",", "."))

        if ptype != "out":
            continue

        if name not in payments_info:
            payments_info[name] = list()

        payments_info[name].append((date[:10], currency, amount))

    return payments_info


# def get_currencies(dict):
#     currencies = []
#     for key, value in sorted(dict.items()):
#         i = len(value) - 1
#         c = value[i][1]
#         while i >= 0:
#             if c not in currencies:
#                 currencies.append(c)
#             i -= 1
#     return currencies


def get_dates(info):
    dates = set()
    for key, value in info.items():
        value_dates = set([p[0] for p in value])

        # for d in value_dates:
        #     dates.add(d)

        # [dates.add(d) for d in value_dates]
        dates |= value_dates

    return sorted(list(dates))


def first_assignment(info):
    # info = {key: "NAME", value: [('DATE','CURRENCY', 'SPEND')]}
    # Полчучить список людей и сумму всех покупок в каждой валюте и кол-вом покупок
    with open('first_assignment.txt', "w") as f1:
        for key, value in sorted(info.items()):
            # теперь нам просто нужно разделить список value на два списка, с разными валютами.
            # для этого очень удобно использовать списковые выражения или генераторные
            # и потом просто передать в функцию sum для подсчета суммы
            # всегда старайтесь использовать sum в таких случаях
            # если вы в цикле суммируете элементы списка - самое время для sum
            usd_spends = [p[2] for p in value if p[1] == "USD"]
            eur_spends = [p[2] for p in value if p[1] == "EUR"]

            spends = {'USD': sum(usd_spends), 'EUR': sum(eur_spends)}

            item = "{0} - {1} in USD - {2} in EUR - {3} purchases.".format(key, round(spends['USD'], 2), round(spends['EUR'], 2), len(value))
            f1.writelines('\n' + item)


def second_assignment(info):
    # info = {key: "NAME", value: [('DATE','CURRENCY', 'SPEND')]}
    # Получить список людей, которые тратили каждый день
    with open('second_assignment_ksu.txt', "w") as f2:
        for key, value in sorted(info.items()):
            # получить даты для текущей записи, то есть персоны - уникальные, те через set
            key_dates = set([p[0] for p in value])

            if len(key_dates) == len(get_dates(info)):
                item = "{0} - {1}".format(key, sorted(key_dates))
                f2.writelines('\n' + item)


def third_assignment(info):
    # info = {key: "NAME", value: [('DATE','CURRENCY', 'SPEND')]}
    with open('third_assignment.txt', "w+") as f3:
        for key, value in sorted(info.items()):
            key_dates = []
            i = len(value) - 1
            while i >= 0:
                for date in get_dates(info):
                    if date not in key_dates:
                        if value[i][0] == date:
                            key_dates.append(value[i][0])
                i -= 1
            if len(key_dates) == 1 and value[i][0] == get_dates(info)[0]:
                item = "{0} - {1}".format(key, sorted(key_dates))
                f3.writelines('\n' + item)



path = "payments"
d = take_content(path)
# print(get_dates(d))
# print(d)
# first_assignment(d)
second_assignment(d)
# third_assignment(d)
