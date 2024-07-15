def checarOrdem(lista, index, maior, bool):
    if(index > len(lista)-1):
        return bool
    else:
        if(lista[index] >= maior):
            return checarOrdem(lista, index+1, lista[index], )

def ordenada(lista):