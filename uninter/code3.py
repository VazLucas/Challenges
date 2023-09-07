#Iniciando código com a importação do necessário para trazer a função randint 
from random import randint
#Definida a função 'subscription', responsável por receber os dados do usuário e inserir no 'dictionary = pessoas'
def subscription():
  number = randint(100, 400) #gerado de um número aleatório
  pessoas['Voucher'] = number 
  voucherlist.append(number) #adição do número do voucher na lista 'voucherlist' para conferir se está repetido ou não
  if len(set(voucherlist)) == len(voucherlist): #se não estiver repetido, a função segue mostrando o número do voucher e continua pedindo os dados
    print('Esse é seu voucher: {}' .format(number))
    pessoas['Nome'] = input('Qual seu nome?')
    pessoas['Celular'] = input('Qual seu celular para contato?')
    pessoas['Email'] = input('Qual seu email para contato?')
    pessoas['Curso'] = input('Qual curso desejado?')
    detalhe()
#Inserção de uma cópia do 'dictionary = pessoas' na 'lista = inscritos', cada vez que a função 'subscription' ocorre
#há uma nova inserção na lista, gerando um segundo item do dictionary
    inscritos.append(pessoas.copy())
    del mysub[:]
    mysub.append(pessoas)
  else: #se o voucher estiver repetido, o programa mostra que está inválido e reinicia a função 'start'
    detalhe()
    print("Número de voucher inválido, reinicie o processo")
    detalhe()
    start()
  
    
#Definição de uma função de quebra de linha apenas
def detalhe ():
    print('-' *45)

#Definição da função 'start', responsável por servir de menu de opções ao usuário. 
#Ela expõe as opções a partir dos 3 primeiros 'print'.
#Depois, entra numa situação de múltipla escolha que confere se o núemro inteiro escolhido na variável 'escolha' bate com um dos requisitos dos 'if' e 'elif'
def start():
  
  print('Escolha 1 para iniciar uma nova inscrição')
  print('Escolha 2 para mostrar as inscrições')
  print('Escolha 3 para mostrar sua inscrição')
  print('Escolha 0 para finalizar')
  escolha = input('Digite aqui o código')
  detalhe()
#Quando o usuário escolhe a opção 1 (Nova Inscrição), a função 'subscription' se inicia e, após sua execução, outra função é ativada: 'start' (o menu de opções)
  if escolha == '1':
    subscription()
    start()
#Quando o usuário escolhe a opção 2 (Visualizar inscrições), entra-se em uma nova mútlipla escolha: 1º é analisado se a 'lista - inscritos' está 
#vazia/false a partir do operador lógico 'not', se for satisfeita, há a impressão na tela da mensagem abaixo e a função 'start' é iniciada novamente.
#2º se o operador lógico 'not' não for satisfeito, ou seja, há qualquer dado dentro da 'lista - inscritos', há a impressão na tela dos dados lá contidos
#e a função 'start' é inciada novamente.
  elif escolha == '2' :
    if not inscritos:
      
      print('Não há inscritos')
      detalhe()
      start()
    else:
      print(*inscritos,sep='\n') 
      detalhe()
      start()
#Quando a escolha é 0, o porgrama é encerrado
  elif escolha == '0' :
    print('Programa encerrado')
#Se qualquer outro número é escolhido, com exceção do 1, 2 e 0, anteriormente explicados, há a impressão na tela de que o usuário escolheu
#uma opção inválida e a função 'start' é reiniciada para que seja escolhida uma nova opção
  elif escolha == '3':
    if not mysub:
      print('Inscrição não feita')
      detalhe()
      start()
    else:
      print(mysub)
    detalhe()
    start()
  else :
    print('Opção inválida. Por favor, selecione 1, 2 ou 0')
    detalhe()
    start()

#Criação da lista 'inscritos', responsável por carregar os dados contigos no dicitionary 'pessoas'
inscritos = []
mysub = []
#Criação da lista 'voucherlist' para adicionar os números válidos gerados pela função randomint, essa foi a única forma que consegui pensar em como
#analisar se um número de voucher foi repetido ou não pelo gerador de números
voucherlist= []
#Criação do dicitionary 'pessoas', para inserir cada nova inscrição
pessoas = {}
#Aqui se dá o início de todo o algoritmo, todas as outras funções e variáveis foram definidas anteriormente para que quando a função 'start'
#fosse "chamada" tudo estivesse em perfeita ordem para sua execução
start()
