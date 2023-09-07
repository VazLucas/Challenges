# O programa se inicia pedindo que o usuário insira um dado, o qual é seu nome
nome = str(input('Digite um nome:'))
# Aqui é gerado o primeiro dado mostrado na tela para o usuário, seu nome em letras maiúsculas a partir da função '.upper'
# Criei uma variável 'y' vazia para ir preenchendo com os caracteres lidos pelo 'for' e alterando as vogais pelos símbolos pré-estabelecidos
y = ''
# Dessa forma o 'for' vai rodar por todo o 'nome' se utilizando do fator 'i', passando de caractere em caractere e verificando se em algum dos 'if' ou 'elif'
# há satisfação dos requisitos entre parênteses. Se os requisitos para as vogais forem preenchidos, os respectivos símbolos são adicionados na variável 'y',
# caso nenhum dos requisitos para as vogais sejam preenchidos, então o algoritmo, simplesmente, reescreve o valor lido da variável 'nome'.
# Assim, a repetição do 'for' vai inserindo os mesmos caracteres ou os símbolos na variável 'y' para cada caractere presente no nome, até o fim
for i in nome:
    if (i == 'a' or i == 'A'):
        y += '@'
    elif (i == 'e' or i == 'E'):
        y += '&'
    elif (i == 'o' or i == 'O'):
        y += '#'
    elif (i == 'i' or i == 'I'):
        y += '!'
    elif (i == 'u' or i == 'U'):
        y += '*'
    else:
        y += i
print(y.upper())
