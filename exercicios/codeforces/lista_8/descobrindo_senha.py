def extractHighestOiliness(oiliness: list):
    highest = 0.0
    for oil in oiliness:
        if(oil > highest):
            highest = oil
    return highest

def getPassword(oiliness: list, qtPassDigits):
    counterDigits = 0
    password = []
    oilinessCopy = oiliness.copy()
    while(counterDigits != qtPassDigits):
        actualHighestOiliness = extractHighestOiliness(oilinessCopy)
        password.append(oiliness.index(actualHighestOiliness))
        oilinessCopy.remove(actualHighestOiliness)
        counterDigits += 1
    return password


results = []
while(True):
    try:
        qtPassDigits = int(input())
        oiliness = list(map(float, input().split()))
        results.append(getPassword(oiliness, qtPassDigits))
    except EOFError:
        break

counterCase = 1
for result in results:
    print(f"Caso {counterCase}: ", *result, sep="")
    counterCase += 1