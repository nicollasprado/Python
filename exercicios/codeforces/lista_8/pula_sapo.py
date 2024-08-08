jumpHeight, qtPipes = map(int, input().split())
pipesHeights = list(map(int, input().split()))

previousIndex = 0
for pipe in pipesHeights[1:]:
    if((pipesHeights[previousIndex] - pipe) > jumpHeight):
        print("GAME OVER")
        break
    elif(pipesHeights[:-1].index(pipe) == pipesHeights[qtPipes-1] and (pipesHeights[previousIndex] - pipe) < jumpHeight):
        print("YOU WIN")