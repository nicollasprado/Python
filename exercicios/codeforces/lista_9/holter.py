qtMeasurements = int(input())

measurements = []
for i in range(0, qtMeasurements):
    measurements.append(int(input()))

measuresSum = 0
for measure in measurements:
    measuresSum += measure

measureAvg = measuresSum//qtMeasurements

diffMeasureCounter = 0
for measure in measurements:
    if(abs(measureAvg - measure) >= measureAvg * 0.1):
        diffMeasureCounter += 1

print(measureAvg)
print(diffMeasureCounter)