def get_text(name):
    return f"Hello my friend {name}"


def decorate(tag_name):
    def p_decorate(func):
        print(func)

        def func_wrapper(*args, **kwds):
            return "<{1}>{0}</{1}>".format(func(*args, **kwds), tag_name)

        return func_wrapper

    return p_decorate


print(get_text("Miki"))

# get_text = decorate("tag")(decorate("div")(get_text))

# print(get_text("Niki"))


@decorate("tag")
@decorate("p")
@decorate("div")
def get_text(name):
    return f"Hello my friend {name}"


print(get_text("Niki"))
