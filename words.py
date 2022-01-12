def print_upper_words(words, must_start_with):
    """ Printing out all the words in the word list in uppercase  """
    for word in words:
        for letter in must_start_with:
            if word.upper().startswith(letter.upper()):
                print(word.upper())
    