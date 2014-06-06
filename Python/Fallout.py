#!/bin/python
from random import choice, randint

def get_num_of_words():
    return randint(5, 15)

def get_word_length():
    return randint(4, 15)

def get_file_length(some_file):
    for index, _ in enumerate(some_file):
        pass
    words_length = index + 1
    return words_length

def random_seek(words_file):
    file_length = get_file_length(words_file)
    index = choice(range(1, file_length))
    words_file.seek(index)

def get_word(words_file, length_of_word):
    for word in words_file:
        if len(word) == length_of_word:
            return word.strip("\n")
    else:
        return get_word(words_file, length_of_word // 2)

def yield_words(words_file, num_of_words, length_of_word):
    for i in range(num_of_words):
        random_seek(words_file)
        yield get_word(words_file, length_of_word)

def compare_words(word1, word2):
    comparison = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 == letter2:
            comparison += 1
    return comparison

def main(word_length):
    words = open("../enable1.txt", "r", encoding="utf-8")
    # Get the length of the file
    num_of_words = get_num_of_words()
    words = [word for word in yield_words(words, num_of_words, word_length + 1)]
    the_word = choice(words)
    for word in words:
        print(word)
    for i in range(4, 0, -1):
        player_choice = input("Guess ({} left)? ".format(i))
        comparison = compare_words(player_choice, the_word)
        print("{}/{} correct".format(comparison, len(the_word)))
        if comparison == len(the_word):
            print("You win!")
            break
    else:
        print("You lose, the correct word was: {}".format(the_word))


if __name__ == "__main__":
    main(5)
