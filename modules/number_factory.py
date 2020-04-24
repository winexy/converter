from classes.Binary import Binary
from classes.Octal import Octal
from classes.Hexadecimal import Hexadecimal


def factory(option):
    return {
        2: Binary,
        8: Octal,
        16: Hexadecimal
    }[option]()
