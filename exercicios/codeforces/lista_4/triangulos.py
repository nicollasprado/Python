def getTriangleType(stick1, stick2, stick3):
    triangleType = ""
    calculation = (stick1 ** 2) + (stick2 ** 2) - (stick3 ** 2)
    if (calculation > 0):
        # acutangulo
        triangleType = "a"
    elif (calculation == 0):
        # retangulo
        triangleType = "r"
    elif (calculation < 0):
        # obtusangulo
        triangleType = "o"
    return triangleType

def canFormTriangle(stick1, stick2, stick3):
    if (stick1 + stick2 > stick3) and (stick1 + stick3 > stick2) and (stick2 + stick2 > stick1):
        return True

stick1, stick2, stick3 = map(int, input().split())

boolCanForm = canFormTriangle(stick1, stick2, stick3)
if (boolCanForm == True):
    print(getTriangleType(stick1, stick2, stick3))
else:
    print("n")

    # Arrumar