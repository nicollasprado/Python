qtLetters = int(input())
text = input()

prevIndex = 0
nextIndex = 2
casesCounter = 0
itIndexesCounted = []
auxIndex = 0
for letter in text[1:]:
    if(nextIndex > len(text)-1):
        break
    itList = [text[prevIndex], letter, text[nextIndex]]
    itIndexes = [prevIndex, prevIndex+1, nextIndex]
    if(text[prevIndex] != text[nextIndex] and 'a' in itList):
        addIndex = 0
        for it in itList:
            auxIndex = prevIndex + addIndex
            if(it == 'a' and auxIndex not in itIndexesCounted):
                casesCounter += 1
                itIndexesCounted.append(auxIndex)
            addIndex += 1
    prevIndex += 1
    nextIndex += 1

print(casesCounter)