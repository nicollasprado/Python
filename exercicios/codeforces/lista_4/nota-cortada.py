# se um dos pedaços possuir estritamente mais da metade da área da nota original, então ele vale 100 reais
lengthBill, heighBill = 160, 70
areaBill = lengthBill * heighBill

def whoGotHundred(baseCut, topCut):
    # 1 == Felix, 2 == Mariza
    whoGot = 0
    if ((80 - baseCut) == (topCut - 80)):
        whoGot = 0
    elif (baseCut == 0) and (topCut == 0):
        whoGot = 0

    elif (baseCut <= 80) and (topCut <= 80):
        whoGot = 2
    elif (baseCut >= 80) and (topCut >= 80):
        whoGot = 1

    elif (baseCut < 80) and (topCut > 80):
        if ((80 - baseCut) > (topCut - 80)):
            whoGot = 2
        elif ((80 - baseCut) < (topCut - 80)):
            whoGot = 1

    elif (baseCut > 80) and (topCut < 80):
        if ((baseCut - 80) > (80 - topCut)):
            whoGot = 1
        elif ((baseCut - 80) < (80 - topCut)):
            whoGot = 2
    return whoGot

def getCuttedArea(baseCut, topCut):
    if (topCut > baseCut):
        rectanglePart = baseCut * 70
        trianglePart = (topCut - baseCut) * 70
        totalCuttedArea = rectanglePart + trianglePart
    elif (baseCut > topCut):
        rectanglePart = topCut * 70
        trianglePart = (baseCut - topCut) * 70
        totalCuttedArea = rectanglePart + trianglePart
    return totalCuttedArea

def verifyCuttedArea(cuttedArea):
    halfBill = areaBill / 2
    if (cuttedArea > halfBill):
        return True

baseCutPointToLeft = int(input())
topCutPointToLeft = int(input())

if (baseCutPointToLeft <= 0) and (topCutPointToLeft <= 0) or (baseCutPointToLeft > 160) or (topCutPointToLeft > 160):
    # raise Exception("Os dois valores não podem ser zero")
    print(0)
else:
    cuttedArea = getCuttedArea(baseCutPointToLeft, topCutPointToLeft)
    if (verifyCuttedArea(cuttedArea) == True):
        print(whoGotHundred(baseCutPointToLeft, topCutPointToLeft))
    else:
        print(0)