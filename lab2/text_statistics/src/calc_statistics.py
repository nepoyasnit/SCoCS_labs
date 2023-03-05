import re
from collections import Counter
from abbreviations import ONE_ABBREVIATIONS, TWO_ABBREVIATIONS


def amount_of_sentences(text: str) -> int:
    regex = r'([.!?]+)'
    sentences_number = len([*re.finditer(regex, text)])
    for abbr in ONE_ABBREVIATIONS:
        if text.find(abbr) != -1:
            sentences_number -= 1

    for abbr in TWO_ABBREVIATIONS:
        if text.find(abbr) != -1:
            sentences_number -= 2

    return sentences_number


def amount_of_non_declarative_sentences(text: str) -> int:
    regex = r'([!?]+)'
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
    regex = r'([.!?]+)'
    sentences = filter(contain_words, re.split(regex, text))
    all_letters = sum(list(map(lambda word: sum(len_of_words(word)), sentences)))
    try:
        return all_letters / amount_of_sentences(text)
    except ZeroDivisionError:
        return 0


def len_of_words(text: str) -> list[int]:
    words = extract_words(text)
    return list(map(lambda word: len(word), words))


def average_len_of_words(text: str) -> float:
    return average(len_of_words(text))


def ngrams(text: str, n: int):
    return [text[i:i + n] for i in range(len(text) - n + 1)]


def k_repeated_ngrams(text: str, k: int = 10, n: int = 4):
    text_ngrams = ngrams(text, n)

    counter = Counter(text_ngrams)
    k_items = counter.most_common(k)

    return k_items
