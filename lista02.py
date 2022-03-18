lista = ['dois']

#lista.append()
print(lista)

lista.append('três') #inserir no final da lista
print(lista)

lista.insert(0,'um') #inserir um item antes de um dado.
print(lista)

lista.sort() #ordenar ordem crescente/alfbetica
print(lista)

lista.sort(reverse=True)#ordenar ordem decrescente
print(lista)

lista.pop(1) #remover determidado item da lista  lembrando que o primeiro item começa no 0
print(lista)

lista .remove('dois')
print(lista)
if 'um' in lista:
    lista.remove('um')

lista =['dois']
lista.insert(0,'um')
lista.append('três')
lista[1]='segundo'
for x in range(0,len(lista)):
    print(str(x+1)+'° item ->'+ lista[x])