
op = 0
def menu():
    op = int(input('Operação desejada: \n' + 
             '1- Listar      | 2- Cadastrar \n' + 
             '3- Alterar     | 4- Excluir \n' + 
             '           5- Sair\n'))
    return op

def listaVazia(obj):
    return len(obj) == 0

def listar(obj):
    if not listaVazia(obj):
        print(obj)
    else:
        print('Lista vazia')

def cadastrar(obj,valor):
    if valor in obj:
        print(valor + ' já está cadastrado')
    else:
        obj.append(valor)
        print(valor + ' cadastrado com sucesso')

def alterar(obj,valor): 
    if not ( valor in obj):
        print(valor + ' não está cadastrado na lista.')
        return
    for x in range(0,len(obj)):
        if obj[x] == valor:
            novo = input('Informe o novo valor para ' + valor + ': ')
            if novo in obj:
                print(novo + ' já está cadastrado.')
            else:                
                obj[x] = novo

def excluir(obj,valor):
    if len(obj) == 0:
        print('A lista está vazia')
    else:
        if valor in obj:
            obj.remove(valor)
            print(valor + ' removido com sucesso!')
        else:
            print(valor + ' não existe na lista')
