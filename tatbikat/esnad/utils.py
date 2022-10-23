import random
import string


def belge_no_yap():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))