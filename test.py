import statistics
import numpy as np
import matplotlib.pyplot as plt

file = open("Europarl.txt", "r", encoding="utf8")
n = 1

wordArray = []
sentenceArray = []
wLength = 0
wCount = 0
countChar = 0
endOfSentence = False

for chunk in iter(lambda: file.read(n), ''):
    countChar += 1
    if countChar % 1000000 == 0:
        print(countChar/1000000)
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

for d in distWord:
    print(d)
