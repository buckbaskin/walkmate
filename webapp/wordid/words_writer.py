import re

if __name__ == '__main__':
    original_words_file = open('/usr/share/dict/words', 'r')

    new_words_file = open('words.txt', 'w')

    write_count = 0

    for word in original_words_file:
        word = word.strip()
        if re.match('^[\w]+$', word) is not None:
            new_words_file.write('%s\n' % (word,))
            write_count += 1

    print('Wrote in %d words' % (write_count,))

    original_words_file.close()
    new_words_file.close()
