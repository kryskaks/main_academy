def get_digits_sum(num):
    # TODO implement recursive function
    pass


def check_natural_number(func):
    # TODO implement decorator-checker
    pass
    # return inner function


@check_natural_number
def call_r_function(num):
    return get_digits_sum(num)


print("result:", call_r_function(1285))  # should be 16
