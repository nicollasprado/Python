def balanceTeams(levelA, levelB, levelC, levelD):
    highestLevel = levelA
    if (levelB > levelA) and (levelB > levelC) and (levelB > levelD):
        highestLevel = levelB
    elif (levelC > levelA) and (levelC > levelB) and (levelC > levelD):
        highestLevel = levelC
    elif (levelD > levelA) and (levelD > levelB) and (levelD > levelC):
        highestLevel = levelD
    
    lowestLevel = levelA
    if (levelB < levelA) and (levelB < levelC) and (levelB < levelD):
        lowestLevel = levelB
    elif (levelC < levelA) and (levelC < levelB) and (levelC < levelD):
        lowestLevel = levelC
    elif (levelD < levelA) and (levelD < levelB) and (levelD < levelC):
        lowestLevel = levelD

    teamA = highestLevel + lowestLevel
    if (highestLevel == levelA) and (lowestLevel == levelB):
        teamB = levelC + levelD
    elif (highestLevel == levelA) and (lowestLevel == levelC):
        teamB = levelB + levelD
    elif (highestLevel == levelA) and (lowestLevel == levelD):
        teamB = levelB + levelC
        
    elif (highestLevel == levelB) and (lowestLevel == levelC):
        teamB = levelB + levelD
        # concluir
    elif (highestLevel == levelA) and (lowestLevel == levelC):
        teamB = levelB + levelD
    elif (highestLevel == levelA) and (lowestLevel == levelC):
        teamB = levelB + levelD
    elif (highestLevel == levelA) and (lowestLevel == levelC):
        teamB = levelB + levelD


levelPA, levelPB, levelPC, levelPD = map(int, input().split())

print(balanceTeams(levelPA, levelPB, levelPC, levelPD))