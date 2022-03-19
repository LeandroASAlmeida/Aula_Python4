# Você deverá implementar um sistema onde seja possível cadastrar, alterar, 
# visualizar e excluir itens de uma lista de produtos de informática
# Deverá ter um menu com as opções para que o usuário informe a opção desejada
# Não poderá inserir itens duplicados
# Caso tente alterar, visualizar ou excluir item inexistente, o sistema deve informar
# isso para o usuário
# A cada iteração deverá limpar a tela e mostrar o menu novamente
# DEVERÁ SER TOTALMENTE FEITO UTILIZANDO SUBROTINAS
# Tempo estimado: 35 minutos. 


listInf = ['mouse','teclado','memoria','estabilizador']

opc = int(input('Cadastrar, digite 1\nAlterar, digite 2 \nExcluir, digite 3 \nConsultar, digite 4 \nOu 5 para Sair \nOpção: '))
print()
if opc == 1:
    prod = input('Digite o nome do produto: ')
    listInf.append(listInf)
    print('Cadastrado com sucesso')

elif opc == 2:
    prod = (listInf())
    listInf
    print('Alterado com sucesso')
elif opc == 3:
    prod = listInf
    listInf.pop(prod)
    print('Produto excluido')
elif opc == 4:
   print([listInf])
else:
    print("Programa finalizado")



















