import math
#en cuanto al calculo de pi el tiempo de proceso y la precision
#dependera del limite proporcionado
lim = 1000000

def calcular(limite):
    suma = 0
    for valor in range (1, limite):
        suma= suma + (1/ valor ** 2)

    pi = math.sqrt(suma * 6)
    return pi

print ("PI es" , calcular(lim))