import random as r


def get_random_login():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    login = ''.join([r.choice(letters) for _ in range(7)])
    return f'{login}@gmail.com'


def get_random_password():
    return r.randint(100000, 999999)
