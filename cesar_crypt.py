import string


# a -> d, b -> e, c -> f ... x -> a, y -> b, z -> c
def get_cesar_map(gap, reverse):
    # создаем тупл ключей, это просто последовательность литер в нижнем регистре
    keys = tuple(string.ascii_lowercase)
    # создаем тупл значение, это тоже последовательность литер
    # но по сравнению с keys, нулевым элементом тупла идет gap-ый элемент из keys
    # первым элементом идет (gap+1)-ый элемент keys и так далее
    values = tuple(keys[gap:] + keys[:gap])

    # в зависимоти от того, нужно ли нам делать шифрование (reverse=False) или дешифрование (reverse=True)
    # формируем нужный словарь
    if reverse:
        cesar_map = dict(zip(values, keys))
    else:
        cesar_map = dict(zip(keys, values))

    return cesar_map


phrase = "hell0 world"

cesar_map = get_cesar_map(3, False)

# проходимся по каждой литере в последовательности phrase и формируем новый список с помощью cesar_map
# и склеиваем этот полученный список литер в строку с помощью join
encrypted = "".join([cesar_map.get(letter, letter) for letter in phrase])

print(encrypted)

cesar_map = get_cesar_map(3, True)

decrypted = "".join([cesar_map.get(letter, letter) for letter in encrypted])

print(decrypted)

print("phrase == decrypted:", phrase == decrypted)
