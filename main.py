'''
# variavel para separar
nome = 'John Connor'

nome_completo = nome.split(' ')

# exibe a lista
for parte_nome in nome_completo:
    print(parte_nome, end=' ')
'''    
nome = input('Informe o seu nome completo: ')    

# separa as palavras do nome e capitula
nome_lista = nome.split(' ')

for i in range(len(nome_lista)):
    nome_lista[i] = nome_lista[i].capitalize()

# junta o nome em uma variável
nome_completo = ' // '.join(nome_lista)

# exibe na tela
print(nome_completo)