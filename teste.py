import subrotinas

subrotinas.time.sleep(5)
if subrotinas.EhPar(10):
    subrotinas.mensagem('Valor é PAR')
else:
    subrotinas.mensagem('Valor é IMPAR')
subrotinas.time.sleep(3)
subrotinas.os.system('cls')