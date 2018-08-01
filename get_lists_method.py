import sys


def main():
    print(sys.argv)

    if len(sys.argv) != 2:
        # ожидается два аргумента командной строки, первый - это имя файла, второй - исследуемый тип
        print("Unexpected argv len")
        return "Unexpected argv len"

    inspected_type = sys.argv[1]
    print(inspected_type, type(inspected_type))

    types_map = {"str": str, "list": list, "dict": dict,
                 "tuple": tuple, "set": set}

    f_obj = None
    # так как нет отдельного типа для файловых объектов, добавляем в file types_map
    # можно будет инспектировать объект f_obj и отображать все его доступные методы
    if inspected_type == "file":
        f_obj = open("calc.py")
        types_map["file"] = f_obj
        # f.close()

    # если inspected_type не является ключом словаря types_map, значит передан некорректный тип, выход из скрипта
    elif inspected_type not in types_map:
        print(f"Unexpected arg: {inspected_type}")
        return

    inspected_type = types_map[inspected_type]

    # получаем список всех атрибутов у исследуемого объекта
    attrs = dir(inspected_type)
    # список с строк для записи в файл
    lines = []
    for attr in attrs:
        # если атрибут начинается с  _, он нас не интересует
        if not attr.startswith("_"):
            # получаем значение по атрибуту attr у исследуемого объекта.
            # Например, str.count, если attr имеет значение "count", str.index, если attr = "index"
            method = getattr(inspected_type, attr)
            lines.append(f"{attr.upper()}\n")
            # у каждого метода есть атрибут __doc__ с его описанием.
            doc = method.__doc__
            lines.append(f"{doc}\n\n")

    file_name = f'{sys.argv[1]}_methods'
    with open(file_name, 'w') as f:
        f.writelines(lines)

    # завершаем работу с файловым объектом, если он был создан
    if f_obj:
        f_obj.close()

    print(f"File {file_name} is ready")


main()
