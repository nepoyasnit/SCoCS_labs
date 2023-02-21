import re


def amount_of_sentences(text: str) -> int:
    regex = r'([.!?] )'
    return len([*re.finditer(regex, text)])


def amount_of_non_declarative_sentences(text: str) -> int:
    regex = r'([!?] )'
    return len([*re.finditer(regex, text)])

