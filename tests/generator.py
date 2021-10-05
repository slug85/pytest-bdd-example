import random


def create_a_phone():
    suffix = random.randint(999999, 10000000)
    return "7900{}".format(suffix)
