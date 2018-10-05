# -*- coding: utf-8 -*-
# 1. Необходимо получить список людей и сумму всех их покупок в каждой валюте и количеством покупок.
# Сначала отсортировать по сумме покупок, а потом по количеству
# 2. Получить список людей которые тратили каждый день.
# 3. Сформировать отдельно список людей, которые тратили деньги только в первый день.


FILES = ("2018-08-20.txt", "2018-08-21.txt", "2018-08-22.txt", "2018-08-23.txt", "2018-08-24.txt")


def parse_file(file_name):
    with open(file_name) as f:
        lines = [parse_line(line) for line in f if "out" in line]
        return lines


def parse_line(line):
    # Remus Lupin;329.76 EUR;2018-08-20 19:36:32;out;
    name, amount_and_currency, date, *_ = line.split(";")
    amount, currency = amount_and_currency.split()
    amount = float(amount.replace(",", "."))
    return name, amount, currency, date


def get_names_from_lines(lines):
    day_names = [l[0] for l in lines]
    return set(day_names)


def get_everyday_payers():
    all_names = get_names_from_lines(parse_file("2018-08-20.txt"))
    for f in ("2018-08-21.txt", "2018-08-22.txt", "2018-08-23.txt", "2018-08-24.txt"):
        lines = parse_file(f)
        names = get_names_from_lines(lines)
        all_names &= names

    return all_names


def get_all_payers():
    all_names = set()
    for f in ("2018-08-20.txt", "2018-08-21.txt", "2018-08-22.txt", "2018-08-23.txt", "2018-08-24.txt"):
        lines = parse_file(f)
        names = get_names_from_lines(lines)
        all_names |= names

    return all_names


def get_first_day_payers_only():
    first_day_payers = get_names_from_lines(parse_file("2018-08-20.txt"))

    for f in ("2018-08-21.txt", "2018-08-22.txt", "2018-08-23.txt", "2018-08-24.txt"):
        lines = parse_file(f)
        names = get_names_from_lines(lines)
        first_day_payers -= names

    return first_day_payers


def get_payers_info():
    all_payers = get_all_payers()

    payers_info = {name: [] for name in all_payers}

    for f in ("2018-08-21.txt", "2018-08-22.txt", "2018-08-23.txt", "2018-08-24.txt"):
        lines = parse_file(f)
        for l in lines:
            name, amount, currency, *_ = l
            payers_info[name].append((amount, currency))

    return payers_info


def get_sorted_total(payers_info):
    def key_func(name):
        info = payers_info[name]

        return sum((amount for amount, curency in info))

    sorted_info = sorted(payers_info, key=key_func)

    print(sorted_info)


def get_sorted_by_count(payers_info):
    def key_func(name):
        info = payers_info[name]

        return len(info)

    sorted_info = sorted(payers_info, key=key_func)

    print(sorted_info)


info = get_payers_info()
print("sorted by total amount")
get_sorted_total(info)

print("sorted by count")
get_sorted_by_count(info)
# daily_payers = get_everyday_payers()
# all_payers = get_all_payers()
# first_day_payers = get_first_day_payers_only()
# [print(n) for n in daily_payers]
# print(len(daily_payers))

# [print(n) for n in all_payers]
# print(len(all_payers))

# print("get_first_day_payers_only")
# [print(n) for n in first_day_payers]
# print(len(first_day_payers))

