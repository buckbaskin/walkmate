from webapp.wordid import integer_to_wordset, wordset_to_integer

upper = 1000000000

next_ = 0.0

for i in range(0, upper, 377):
    if i / float(upper) > next_:
        print('%d%% %d -> %s' % (int(100*i/float(upper)), i, integer_to_wordset(i),))
        next_ += 0.1
    try:
        assert i == wordset_to_integer(integer_to_wordset(i))
    except AssertionError:
        print('failed on example i = %d' % (i,))
        print('to wordset: %s' % (integer_to_wordset(i),))
        print('to integer: %s' % (wordset_to_integer(integer_to_wordset(i),)))
