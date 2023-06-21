from collections import Counter, OrderedDict

words = open("words.txt", "r")
counter = Counter(words.read().lower())

sorted_list = (sorted(counter.most_common()))

[print(i) for i in sorted_list]