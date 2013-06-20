#!/usr/bin/env python

import sys, random

def make_chains(corpus):
    """Takes an input text as a string and returns a dictionary of
    markov chains."""

    chains = {}
    #split() will default to split(" ") - awesome
    word_list = corpus.split()


    for i in range(len(word_list) - 2):
      first_word = word_list[i]
      second_word = word_list[i + 1]
      trailing_word = word_list[i +2]

      index_tuple = (first_word, second_word)

      chains.setdefault(index_tuple, [])
      chains[index_tuple].append(trailing_word)

    return chains

def make_text(chains):
    """Takes a dictionary of markov chains and returns random text
    based off an original text."""
    text_array = []
    size = 20

    seed = random.randint(0, size - 3)# 3 because we want to exclude seed word, next word, and trailing word    
    rand_tuple = random.choice(chains.keys())
    seed_word = rand_tuple[0] 
    next_word = rand_tuple[1]
 
    for i in range(1,size):
      text_array.append(seed_word)
      trailing_word = random.choice(chains[seed_word, next_word])

      seed_word = next_word
      next_word = trailing_word

    return " ".join(text_array)

def main():
    args = sys.argv
    file_path = args[1]
    file = open(file_path)
    corpus = file.read()

    chain_dict = make_chains(corpus)
    random_text = make_text(chain_dict)

    print random_text

if __name__ == "__main__":
    main()
