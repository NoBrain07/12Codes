# 7	Write the definition of a function zero_ending(scores) to add all those values in the list of scores,
#  which are ending with zero and display the sum.


def zero_ending(scores):
    return sum(x for x in scores if x % 10 == 0)


n = [200, 456, 300, 100, 234, 678]

print(zero_ending(n))
