def getPrimoMaior(num):
    divisor = 1
    for testNum in range(num+1, 10000000):
        if(testNum == divisor):
            divisor += 1
        elif(testNum % divisor == 0):
            continue
        elif(divisor == 10000000 and testNum % divisor != 0):
            return testNum
        else:
            divisor += 1

baseNum = int(input())
print(getPrimoMaior(baseNum))