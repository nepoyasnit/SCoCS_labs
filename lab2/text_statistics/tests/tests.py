import unittest

from ..src.calc_statistics import (
    amount_of_sentences,
    amount_of_non_declarative_sentences,
    average_len_of_sentences,
    average_len_of_words,
    k_repeated_ngrams
)


class TestAmountOfSentences(unittest.TestCase):
    def test_1(self):
        self.assertEqual(amount_of_sentences('Hello, World! '), 1)

    def test_2(self):
        self.assertEqual(amount_of_sentences('Hello, Mr.Maks.'), 1)

    def test_3(self):
        self.assertEqual(amount_of_sentences('Hello, Mr. Maks!? '), 1)

    def test_4(self):
        self.assertEqual(amount_of_sentences('Hello, Dr. Maks. '), 1)

    def test_5(self):
        self.assertEqual(amount_of_sentences('Hello, Mrs. Maxwell...'), 1)

    def test_6(self):
        self.assertEqual(amount_of_sentences('There is some great news when it comes to job interviews. It’s not all '
                                             'doom and gloom (bad). Most recruiters these days ask the interviewees ('
                                             'you) the same basic questions.'), 3)

    def test_7(self):
        self.assertEqual(amount_of_sentences(''), 0)

    def test_8(self):
        self.assertEqual(amount_of_sentences('1231.'), 1)


class TestAverageLengthOfWords(unittest.TestCase):
    def test_1(self):
        self.assertEqual(average_len_of_words('Another sentence.'), 7.5)

    def test_2(self):
        self.assertEqual(average_len_of_words('My strange sentence.'), 17/3)

    def test_3(self):
        self.assertEqual(average_len_of_words(''), 0)

    def test_4(self):
        self.assertEqual(average_len_of_words('Hello!'), 5)

    def test_5(self):
        self.assertEqual(average_len_of_words('M'), 1)


class TestAverageLengthOfSentence(unittest.TestCase):
    def test_1(self):
        self.assertEqual(average_len_of_sentences('Hello Mr. Maks! Im a driver.'), 10)

    def test_2(self):
        self.assertEqual(average_len_of_sentences('Hello!'), 5)

    def test_3(self):
        self.assertEqual(average_len_of_sentences(''), 0)

    def test_4(self):
        self.assertEqual(average_len_of_sentences('1.'), 0)

    def test_5(self):
        self.assertEqual(average_len_of_sentences(' '), 0)


class TestAmountOfNonDeclarative(unittest.TestCase):
    def test_1(self):
        self.assertEqual(amount_of_non_declarative_sentences('Hello Mr. Maks! Im a driver.'), 1)

    def test_2(self):
        self.assertEqual(amount_of_non_declarative_sentences('H!'), 1)

    def test_3(self):
        self.assertEqual(amount_of_non_declarative_sentences(''), 0)

    def test_4(self):
        self.assertEqual(amount_of_non_declarative_sentences('I.'), 0)

    def test_5(self):
        self.assertEqual(amount_of_non_declarative_sentences('Hello!!!!!!!'), 1)


class TestNGrams(unittest.TestCase):
    def test_1(self):
        self.assertEqual(k_repeated_ngrams('Hello, Maks!', 10, 3),
                         [('Hel', 1), ('ell', 1), ('llo', 1), ('lo,', 1), ('o, ', 1),
                          (', M', 1), (' Ma', 1), ('Mak', 1), ('aks', 1), ('ks!', 1)])

    def test_2(self):
        self.assertEqual(k_repeated_ngrams('', 100, 100), [])

    def test_3(self):
        self.assertEqual(k_repeated_ngrams('H', 1, 1), [('H', 1)])

    def test_4(self):
        self.assertEqual(k_repeated_ngrams('Hello!', 0, 0), [])
