
import collections
from itertools import count
from string import ascii_letters
from tkinter.tix import LabelEntry
from collections import Counter, OrderedDict

words = open("words.txt", "r")
counter = Counter(words.read())
#print(counter.most_common())
counter["a"]

class OrderedCounter(Counter, OrderedDict):
 pass

#oc = OrderedCounter(ascii_letters)

list = (OrderedDict(counter))

#print(sorted(counter.most_common()))
sorted_list = (sorted(counter.most_common()))

#print(sorted_list)

a = sorted_list
#[print(i, end=' ') for i in a]
[print(i) for i in a]