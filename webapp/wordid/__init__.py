words_forward = {} # number to word
words_backward = {} # word to number

import math


with open('webapp/wordid/words.txt', 'r') as words_file:
    for index, word in enumerate(words_file):
        if word.strip() == '':
            pass
        words_forward[index] = word.strip()
        words_backward[word.strip()] = index

def integer_to_wordset(integer):
    integer = int(integer)
    integer = abs(integer)
    num_options = len(words_forward)

    num_words = math.ceil(math.log2(integer+1)/math.log2(num_options))
    if num_words <= 0:
        num_words = 1
    # print('num_words %d' % (num_words,))

    words_out = []

    for i in range(0, num_words):
        offset = math.pow(num_options, i)
        index = (integer // offset) % num_options
        # print('next_word %s' % (words_forward[index]))
        words_out.append(words_forward[index])

    return '.'.join(words_out)

def wordset_to_integer(wordset):
    wordset = str(wordset)
    words = wordset.split('.')

    accum = 0

    for index, word in enumerate(words):
        if word in words_backward:
            accum += words_backward[word] * math.pow(len(words_backward), index)

    return int(accum)
