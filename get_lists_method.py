import sys


def main():
    attrs = dir(list)
    lines = []
    for attr in attrs:
        if not attr.startswith("__"):
            method = getattr(list, attr)
            print(method)
            lines.append(f"{attr.upper()}\n")
            doc = method.__doc__
            lines.append(f"{doc}\n\n")
    print(lines)
    with open('list_methods', 'w') as f:
        f.writelines(lines)


main()
