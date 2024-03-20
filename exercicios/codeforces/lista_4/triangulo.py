def possoCriarUmTriangulo(varetas: list):
    minIndex = 0
    maxIndex = 2
    proxVaretaIndex = maxIndex + 1
    resultado = 'N'
    while (maxIndex < 4):
        if maxIndex == 4:
            proxVaretaIndex = 3
        somaDoisPrimeirosVal = sum(varetas[minIndex:maxIndex])
        if somaDoisPrimeirosVal > varetas[proxVaretaIndex]:
            resultado = 'S'
            break
        else:
            minIndex += 1
            maxIndex += 1
    return resultado
    

vareta1, vareta2, vareta3, vareta4 = map(int, input().split())
varetas = [vareta1, vareta2, vareta3, vareta4]

print(possoCriarUmTriangulo(sorted(varetas)))