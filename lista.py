lista = ["2324", "teste", "robervan"]
# lista array

# thislistqqqq = list(('teste', 'teste', 'robervan'))
# print(thislistqqqq)
# lista.append("auriene")
# adicionar novos itens no final da lista, usando o método append()
lista.append(20)
# lista.pop(-1) # pop remove elemento da lista da posição

print('quantidade de itens da lista: ', len(lista),
      "Itens")  # Com o comando LEN você consegue saber quantidade de intens em um array itens de um array

lista.insert(2, 'insere')  # insere um elemento na lista na posição 2 ou pode ser no inicio

# REMOVE

lista.remove("teste")
ultimo = lista.pop()
print('ultimo elemento removido foi:', ultimo)  # remove o ultimo element

print(lista)
#    consultar elementos de uma lista, tamanho


print(type(lista))

listaTeste = ['2,', '3', '4', '5', '6']

print('menor munero da lista', (min(listaTeste)))

#  consulta se item existe na lista
print('robervn' in lista)  # Retorna true ou false.

# AULA DICIONARIOS
alvo = {
    'ip': '191.168.0.143',
    'ativo': True,
    'portas': [10, 20, 30],
}

print(alvo['ip'] + ' Ip encontrado ')  # ? procura item dentro da lista

# ADICIONAR VALOR ou atualizar
alvo2 = {
    'ip': '191.168.0.14553',
    'so': "robervan",
    'ativo': True,
    'portas': [10, 20, 390],
}
print('##############')
alvo2['so'] = 'adicionar'
# REMOVER ITENS
print('##############')
alvo2.pop('portas')
# OUTRA FORMA DE LER
print('##############')
print(alvo2.values())  # Traz tudo
print(alvo2.keys())  # ?  traz somente as descrição

# LINK TABELA DE ATALHO: resources.jetbrains.com/storage/products/pycharm/docs/PyCharm_ReferenceCard.pdf
