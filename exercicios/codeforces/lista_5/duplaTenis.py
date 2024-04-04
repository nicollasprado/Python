def balanceTeams(levels: list):
    teamA = levels[0] + levels[3]
    teamB = levels[1] + levels[2]
    return (teamA - teamB)


levelPA, levelPB, levelPC, levelPD = map(int, input().split())
levels = sorted([levelPA, levelPB, levelPC, levelPD])

print(balanceTeams(levels))