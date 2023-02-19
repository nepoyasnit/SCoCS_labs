def find_even(numbers: list):
    even_numbers = []

    for element in numbers:
        if element % 2 == 0:
            even_numbers.append(element)

    return even_numbers
