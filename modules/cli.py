# coding=utf-8
from config import constants
from number_factory import factory


def start():
    greet()
    should_continue = True
    while should_continue:
        print_options()
        option = input_option()

        if option not in constants.VALID_OPTIONS:
            break

        print_internal_options()
        operation = int(input("Select operation: "))

        instance = factory(option)

        if operation == 1:
            value = raw_input(wrap_color("Input value: "))
            direction = input_direction()

            print instance.convert(value, direction)
        elif operation == 2:
            lhs = raw_input("Number 1: ")
            rhs = raw_input("Number 2: ")
            print instance.plus(lhs, rhs)

    say_goodbye()


def print_options():
    options = "\n" \
              "2: Binary\n" \
              "8: Octal\n" \
              "16: Hexadecimal\n" \
              "Press any key to exit\n"

    print wrap_color(options)


def print_internal_options():
    options = "\n" \
              "1: Convert\n" \
              "2: Plus\n"

    print wrap_color(options)


def say_goodbye():
    print wrap_color("good bye 😢")


def input_option():
    option = raw_input(wrap_color("Select option: "))
    try:
        option = int(option)
    finally:
        return option


def input_direction():
    direction = int(raw_input(wrap_color("1: To decimal\n2: From decimal\n")))
    return direction == constants.FROM_DECIMAL


def wrap_color(text):
    return constants.BOLD + constants.OKBLUE + text + constants.ENDC


def greet():
    print wrap_color("hola 🙂")