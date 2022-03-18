import os 
import time

def mensagem(pValor):
    print(pValor)

def mensagem2():
    print('Seja bem vindo')

def somaValores(pValor1, pValor2 = 0, pValor3 = 1):
    print('A soma dos valores é ' + str(pValor1 + pValor2 + pValor3))

def EhPar(pValor):
    def ValidaResult(pOpcao):
        if pOpcao == 1:
            return 'Valor é Verdadeiro'
        return 'Valor é Falso'
    if type(pValor) is str:
        print('Valor inválido')
        return
    if pValor % 2 == 0:
        print(ValidaResult(1))
        return True
    print(ValidaResult(2))
    return False

if EhPar('4'):
    print('valor é par')
else:
    time.sleep(3)
    os.system('cls')
    print('Valor não é par')
    time.sleep(4)
    os.system('cls')