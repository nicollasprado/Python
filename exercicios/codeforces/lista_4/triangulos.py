def getTriangleType(sticks: list):

    return sticksRad

def canFormTriangle(stick1, stick2, stick3):
    if (stick1 + stick2 > stick3) and (stick1 + stick3 > stick2) and (stick2 + stick2 > stick1):
        return True

stick1, stick2, stick3 = map(int, input().split())
sticks = [stick1, stick2, stick3]

boolCanForm = canFormTriangle(stick1, stick2, stick3)
if (boolCanForm == True):
    print(getTriangleType(sticks))
    print(getLongestStick(sticks))
    print(getMediumStick(sticks))

    # https://www.youtube.com/watch?v=tmY8VNp1gWk