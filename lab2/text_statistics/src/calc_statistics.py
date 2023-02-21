import re


def amount_of_sentences(text: str) -> int:
    regex = r'([.!?] )'
    return len([*re.finditer(regex, text)])
