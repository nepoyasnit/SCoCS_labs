from calc_statistics import amount_of_sentences, amount_of_non_declarative_sentences, \
    average_len_of_words, average_len_of_sentences

TEST_STR = 'Hello, man! User.com wants to say that he died... Can u call me?! '


def main():
    print(amount_of_sentences(TEST_STR))
    print(amount_of_non_declarative_sentences(TEST_STR))
    print(average_len_of_words(TEST_STR))
    print(average_len_of_sentences(TEST_STR))


if __name__ == '__main__':
    main()
