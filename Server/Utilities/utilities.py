import string
import random


def random_str(length=6):
    return ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(length)])