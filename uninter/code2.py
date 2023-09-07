#Instruções para o jogo
print('Olá, bem-vindo(a) ao jogo: Hotel dos Animais')
print('Sua missão é alocar os hóspedes seguindo as seguinte regras:')
print('Cão não pode ficar ao lado de gato.')
print('Cão não pode ficar ao lado de osso.')
print('Gato não pode ficar ao lado de rato.')
print('Rato não pode ficar ao lado de queijo.')
print('Quartos indisponíveis já possuem hóspedes')
print('G – GATO')
print('C – CÃO')
print('R – RATO')
print('O – OSSO')
print('Q – QUEIJO')
print('* - QUARTO INDISPONÍVEL')
print('- - QUARTO DISPONÍVEL')
print('           ----------------(1ª fase)--------------       ')
print('           ----------------BOA SORTE--------------       ')
print('Primeiro, posicione o gato e o rato')

print('[ * | * | - | G ]')
print('[ R | - | * | * ]')

rato = int(input('Em qual quarto deseja colocar o rato? '))
gato = int(input('Em qual quarto deseja colocar o gato? '))

#Primeiro 'if' é para analisar a composição da primeira fase a partir dos dados inseridos pelo jogador
#Assim, o 'if' tem como parâmetro as combinações possíveis de dados inseridos 
if (rato == 6 and gato == 3): 

  print('Parabéns, você conseguiu!')

  print('            ----------------(Fase 2)--------------       ')

  print('Nesta fase voçê deve alocar um CÃO, um OSSO e outro CÃO nos quartos possíveis')
 
  print('[ - | * | * | * ]')
  print('[ * | C | - | - ]') 

 
  cao1 = int(input('Em qual quarto quer colocar o primeiro cão? '))
  osso = int(input('Em qual quarto quer colocar o osso? '))
  cao2 = int(input('Em qual quarto quer colocar o segundo cão? '))

#Primeiro 'if' é para analisar a composição da segunda fase a partir dos dados inseridos pelo jogador
#Assim, o 'if' tem como parâmetro as combinações possíveis de dados inseridos
  if((osso == 1 and cao1 == 7 and cao2 == 8) or (osso == 1 and cao1 == 8 and cao2 == 7)):
    print(                  'Parabéns, você conseguiu!'              )
    print('            ----------------(Fase 3)--------------       ')
    print('Agora sua missão é alocar um gato, um osso e um rato. ')
    
    print('[ - | * | * | * ]')
    print('[ - | G | - | * ]')

    gato = int(input('Onde deseja colocar o gato? '))
    osso = int(input('Em que lugar vai colocar o osso? '))
    rato = int(input('E o rato? '))
     
#Primeiro 'if' é para analisar a composição da terceira fase a partir dos dados inseridos pelo jogador
#Assim, o 'if' tem como parâmetro as combinações possíveis de dados inseridos
    if(rato == 1 and osso == 5 and gato == 7):
      print('                    Parabéns, você conseguiu!            ')
      print('            ----------------(Fase 4)--------------       ')
         
      print('Agora sua missão é alocar dois queijos e um osso')
      print('[ - | - | - | * ]')
      print('[ * | R | * | * ]')
                   
      queijo = int(input('Onde deseja colocar o primeiro queijo? '))
      osso = int(input('Em que lugar vai colocar o osso? '))
      queijo2 = int(input('E o último queijo vai? '))

#Primeiro 'if' é para analisar a composição da quarta fase a partir dos dados inseridos pelo jogador
#Assim, o 'if' tem como parâmetro as combinações possíveis de dados inseridos
      if((osso == 2 and queijo == 3 and queijo2 == 1) or (osso == 2 and queijo == 1 and queijo2 == 3)):
        print('------PARABÉNS, VOCÊ CHEGOU AO FIM DO JOGO!------')
        print('------E VOCÊ...------')
        print('------GANHOOOU!------')
      else: #saída do quarto 'if' se o parâmetro for false
        print('GAME OVER!!')
    else: #saída do teceiro 'if' se o parâmetro for false
      print('GAME OVER!!')
  else: #saída do segundo 'if' se o parâmetro for false
    print('GAME OVER!!')   
else: #saída do primeiro 'if' se o parâmetro for false
  print('GAME OVER!!')
