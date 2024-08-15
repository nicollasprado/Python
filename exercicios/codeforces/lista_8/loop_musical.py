def getPeaks(amplitudes: list):
    amplitudeIterations = []
    peaksCounter = 0
    nextIndex = 1
    for amplitude in amplitudes:
        if(nextIndex > len(amplitudes)-1):
            nextIndex = 0
        if(amplitude > amplitudes[nextIndex]):
            amplitudeIterations.append("DESCIDA")
            nextIndex += 1s
        elif(amplitude < amplitudes[nextIndex]):
            amplitudeIterations.append("SUBIDA")
            nextIndex += 1
        else:
            continue

    itNextIndex = 1
    for it in amplitudeIterations:
        if(itNextIndex > len(amplitudeIterations)-1):
            break
        elif(it == amplitudeIterations[itNextIndex]):
            continue
        else:
            peaksCounter += 1
    return peaksCounter

userInput = 1
results = []
while(userInput != 0):
    qtSamples = int(input())
    userInput = qtSamples
    if(qtSamples == 0): break
    amplitudes = list(map(int, input().split()))
    results.append(getPeaks(amplitudes))

print(results)