dia_semana=('Domingo','Segunda-feira', 'Terça-feira','Quarta-feira','Quinta-feira','Sexta-feira','Sabado')# valores fixos
print(type(dia_semana))
print(dia_semana)
for x in range(0,len(dia_semana)):
    print(dia_semana[x].replace('-feira',''))#manipulação de string

pessoas = ('joao', 'maria','leandro','fabio','paulo','leandro')
print(pessoas)
print(pessoas.count('leandro'))