jumpHeight, qtPipes = map(int, input().split())
pipesHeights = list(map(int, input().split()))

previousIndex = 0
for pipe in pipesHeights[1:]:
    if((abs(pipesHeights[previousIndex] - pipe)) > jumpHeight):
        print("GAME OVER")
        break
    elif(abs((pipesHeights[previousIndex] - pipe)) <= jumpHeight):
        print("YOU WIN")
        break
    else:
        previousIndex += 1