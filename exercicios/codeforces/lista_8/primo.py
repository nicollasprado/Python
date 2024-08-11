def getPrimoMaior(num):
    primo = False
    testNumber = num+1
    while(primo == False):
        for num in range(testNumber-1, 1):
            print(num)
            if(testNumber % num == 0):
                primo = True
        testNumber += 1

baseNum = int(input())
print(getPrimoMaior(baseNum))