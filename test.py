import statistics
import numpy as np
from matplotlib.pyplot import *

file = open("Europarl.txt", "r", encoding="utf8")
n = 1

wordArray = []
sentenceArray = []
wLength = 0
wCount = 0
countChar = 0
endOfSentence = False
calcGraph = 0

for chunk in iter(lambda: file.read(n), ''):
    countChar += 1
    if countChar % 10000000 == 0:
        calcGraph = countChar/1000000
        break

    if chunk == " ":
        wCount += 1
        if wLength != 0:
            wordArray.append(wLength)
            wLength = 0
    elif chunk == "\n":
        if not endOfSentence:
            wCount += 1
            sentenceArray.append(wCount)
            wCount = 0
        endOfSentence = False
    elif chunk in (".", "?", "!"):
        sentenceArray.append(wCount)
        wCount = 0
        endOfSentence = True
    elif chunk in (",", ";", "(", ")", "/", "+", "-", "%", "$", "§", "#"):
        wCount += 1
    else:
        wLength += 1

print("Mean / Variance of Words")
print(statistics.mean(wordArray))
print(statistics.variance(wordArray))
print("Mean / Variance of Sentences")
print(statistics.mean(sentenceArray))
print(statistics.variance(sentenceArray))

maxSentenceLength = max(sentenceArray)
maxWordLength = max(wordArray)
print(maxWordLength)
print(maxSentenceLength)

distSentence = [0] * (maxSentenceLength + 1)
distWord = [0] * (maxWordLength + 1)

for s in sentenceArray:
    distSentence[s] += 1

for w in wordArray:
    distWord[w] += 1

distSentence = distSentence[:150]
distWord = distWord[:20]

xlocations = np.array(range(len(distWord)))+0.5
width = 1
bar(xlocations, distWord, width=width)
yticks(np.arange(0, max(distWord), 10000*calcGraph))
xticks(xlocations + width/2, np.arange(0, len(distWord) + 1, 1))
title("Word Length Distribution")
gca().get_xaxis().tick_bottom()
gca().get_yaxis().tick_left()

#np.arange(0, len(distWord) + 1, 1
show()

#xlocations = np.array(range(len(distSentence)))+0.5
#width = 1
#bar(xlocations, distSentence, width=width)
#yticks(np.arange(0, max(distSentence), 15*calcGraph))
#xticks(np.arange(0, len(distSentence) + 1, 20))
#title("Sentence Length Distribution")
#gca().get_xaxis().tick_bottom()
#gca().get_yaxis().tick_left()