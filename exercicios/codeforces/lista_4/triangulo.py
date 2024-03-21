def possoFormarTriangulo(varetas: list):
    resultado = 'N'
    index = 1
    for vareta in varetas:
        index1 = index + 1
        index2 = index + 2
        if (index1 == 4):
            index1 = 0
        if (index2 == 5):
            index2 = 1
        elif (index2 == 4):
            index2 = 0
        else:
            if (vareta + varetas[index] > varetas[index1]) and (vareta + varetas[index1] > varetas[index]) and (varetas[index] + varetas[index1] > vareta):
                resultado = 'S'
                break
            elif (vareta + varetas[index] > varetas[index2]) and (vareta + varetas[index2] > varetas[index]) and (varetas[index] + varetas[index2] > vareta):
                resultado = 'S'
                break
            else:
                index += 1
                continue
    return resultado
            
    
vareta1, vareta2, vareta3, vareta4 = map(int, input().split())
varetas = [vareta1, vareta2, vareta3, vareta4]

print(possoFormarTriangulo(varetas))