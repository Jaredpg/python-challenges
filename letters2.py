
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

oc = OrderedCounter(ascii_letters)

list = (OrderedDict(counter))

print(sorted(counter.most_common()))
