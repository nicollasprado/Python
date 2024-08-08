timeDecease, initialMass = map(int, input().split())

mass = initialMass
counterSeconds = 0
while(mass > 0.5):
    counterSeconds += timeDecease
    mass = mass/2

minutes = 0
while(counterSeconds >= 60):
    counterSeconds = counterSeconds - 60
    minutes += 1

hours = 0
while(minutes >= 60):
    minutes = minutes - 60
    hours += 1

days = 0
while(hours >= 24):
    hours = hours - 24
    days += 1

hours = '{:02d}'.format(hours)
minutes = '{:02d}'.format(minutes)
counterSeconds = '{:02d}'.format(counterSeconds)
totalTimeToDecease = f"{days} dias {hours}:{minutes}:{counterSeconds}"
print(totalTimeToDecease)