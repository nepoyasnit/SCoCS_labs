from calc_statistics import amount_of_sentences, amount_of_non_declarative_sentences, \
    average_len_of_words, average_len_of_sentences, k_repeated_ngrams


def main():
    text = input('Enter your text(please, be carefully with abbreviations!): ')
    print('Amount of sentences in the text: ', amount_of_sentences(text))
    print('Amount of the non-declarative sentences in the text: ', amount_of_non_declarative_sentences(text))
    print('Average length of the word in the text in chars: ', average_len_of_words(text))
    print('Average length of the sentence in chars(words count only): ', average_len_of_sentences(text))

    try:
        n, k = map(int, input('Enter N and K to get top-K repeated N-grams in the text: ').split())
        print('Top-k repeated N-grams in the text: ', k_repeated_ngrams(text, k, n))
    except ValueError:
        print('Invalid input!')


if __name__ == '__main__':
    main()
