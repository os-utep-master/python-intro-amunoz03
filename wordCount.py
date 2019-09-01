import sys
from collections import *
import re

with open(sys.argv[1], 'r') as fin:
    lines = fin.read()

wordCounts = Counter(re.findall(r"\b\w+\b", lines.lower()))
wordList = list(wordCounts.items())
wordList.sort()

with open(sys.argv[2], 'w') as fout:
    for word, count in wordList:
        fout.write("%s %s\n" % (word,count))