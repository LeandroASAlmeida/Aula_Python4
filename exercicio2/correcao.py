# Você deverá implementar um sistema onde seja possível cadastrar, alterar, 
# visualizar e excluir itens de uma lista de produtos de informática
# Deverá ter um menu com as opções para que o usuário informe a opção desejada
# Não poderá inserir itens duplicados
# Caso tente alterar, visualizar ou excluir item inexistente, o sistema deve informar
# isso para o usuário
# Ao alterar, deverá pedir qual item deseja alterar e para qual nome
# Caso o novo nome esteja já cadastrado, não permitir
# A cada iteração deverá limpar a tela e mostrar o menu novamente
# DEVERÁ SER TOTALMENTE FEITO UTILIZANDO SUBROTINAS
# Por questões de organização, as rotinas do CRUD deverão estar em um arquivo 
# separado e específico
# Tempo estimado: 35 minutos. 
import funcoesCRUD

lista = []
opcao = 0
while ( opcao != 5 ):
    opcao = funcoesCRUD.menu()
    match opcao:
        case 1:
            funcoesCRUD.listar(lista)
        case 2:
            item = input('Item que deseja cadastrar: ')
            funcoesCRUD.cadastrar(lista,item)
        case 3:
            item = input('Valor: ')
            funcoesCRUD.alterar(lista,item)
        case 4:
            if len(lista) == 0:
                print('Lista Vazia')
            else:
                item = input('Informe o item que deseja excluir: ')
                funcoesCRUD.excluir(lista,item)
        case 5:
            print('Obrigado')
