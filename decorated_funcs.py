def spy(func):
    # TODO decorator implementation
    pass


# @spy
def create_dict(*args, **kwds):
    result = dict(kwds)
    for index, arg in enumerate(args):
        result.update({index: arg})

    return result


def create_list(*args, **kwds):
    result = list(args)
    result.extend(kwds.values())
    return result


def create_tuple(*args):
    return tuple(args)


def my_sort(seq_to_sort, key_func=None):
    return sorted(seq_to_sort, key=key_func)


print(create_dict("Ksu", "Ann", "Mary", name="Me", position="developer"))
t = create_tuple(1, 2, 3, 4)
print(t)

print(my_sort(t, key_func=hash))

# TODO add anther function calls, with different parameters
