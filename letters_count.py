import string


def main():
    phrase = """The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense."""

    splitted = phrase.split()
    splitted = [item.strip(string.punctuation) for item in splitted]
    text = "".join(splitted).lower()
    # print(text)
    counter = {key: 0 for key in string.ascii_lowercase}
    counter2 = {}
    # print(counter)
    for letter in text:
        counter[letter] += 1
        if letter in counter2:
            counter2[letter] += 1
        else:
            counter2[letter] = 1

    print(counter)
    print(counter2)

    # items = list(counter.items())
    # print(items[:4])

    # sorted_items = sorted(items, key=lambda x: x[1], reverse=True)
    # print(sorted_items)
    # print(dict(sorted_items))


main()
