import re


def amount_of_sentences(text: str) -> int:
    regex = r'([.!?] )'
    return len([*re.finditer(regex, text)])


def amount_of_non_declarative_sentences(text: str) -> int:
    regex = r'([!?] )'
    return len([*re.finditer(regex, text)])


def average(numbers: list[float]) -> float:
    if not numbers:
        return 0

    return sum(numbers) / len(numbers)


def extract_words(text: str) -> list[str]:
    regex = f'\w*[a-zA-Z]\w*'
    words = re.findall(regex, text)
    return words


def contain_words(text: str) -> bool:
    return bool(extract_words(text))


def average_len_of_sentences(text: str) -> float:
    regex = r'([.!?] )'
    sentences = filter(contain_words, re.split(regex, text))
    return average(list(map(lambda word: sum(len_of_words(word)), sentences)))


def len_of_words(text: str) -> list[int]:
    words = extract_words(text)
    return list(map(lambda word: len(word), words))


def average_len_of_words(text: str) -> float:
    return average(len_of_words(text))
