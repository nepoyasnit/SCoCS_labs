from hello import greetings
from calculations import calculate, DIV_OPERATOR
from even_finder import find_even


def main():
    greetings()

    first_number = 1
    second_number = 0
    operator = DIV_OPERATOR
    test_list = [1, 2, 3, 4]

    try:
        print(calculate(first_number, second_number, operator))
    except (TypeError, ZeroDivisionError) as err:
        print(err)

    try:
        print(find_even(test_list))
    except (TypeError, ZeroDivisionError) as err:
        print(err)


if __name__ == '__main__':
    main()
