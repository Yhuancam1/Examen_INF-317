from multiprocessing import Pool

def es_palindromo (p):
    estandar = str(p).lower().replace(' ', '')
    return estandar == estandar [::-1]

def palindromo (p):
        resultado = es_palindromo (p)
        if(resultado==True):
            resultado = 'Verdad'
        else:
            resultado = 'Falso'
        return (resultado)

if __name__=='__main__':
    pali = [1221,456,'sosos','casa','samas','reconocer',123321,'rayar','mama','anita lava la tina','oso','sumus','troll','rever']
    print(Pool().map(palindromo,pali))