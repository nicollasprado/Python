def getMonoAlgarismNum(num):
    numRes = 0
    auxIndex = 0
    while(len(str(numRes)) > 1 and auxIndex == len(num)-1):
        if(auxIndex > len(str(numRes))):
            auxIndex = 0
        numRes += int(str(num)[auxIndex])
        auxIndex += 1
    return numRes

results = []
while True:
    numA, numB = map(int, input().split())
    if(numA == 0 and numB == 0):
        break
    numAres = getMonoAlgarismNum(numA)
    numBres = getMonoAlgarismNum(numB)
    print(numAres, "-", numBres)
    higher = 1
    if(numBres > numAres):
        higher = 2
    results.append(higher)
    
print(results)