from random import randint


def generate_ramdom_array(n, min_value=None, max_value=None):
    assert min_value < max_value, "Min value should be less than max value"
    values = []
    for i in range(n):
        values.append(randint(min_value, max_value))
    return values
