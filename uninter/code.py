#Antes de iniciar o programa, escolhi definir uma função com o nome 'matrícula', assim seria possível retornar e refazê-la sempre que pedido

def matricula ():
#Aqui o usuário precisa inserir 2 dados, um para o nome do aluno (string) e outro para a idade (inteiro)
  nome = input('Por favor, digite o nome do(a) aluno(a):')
  idade = int(input('Por favor, agora digite a idade do(a) aluno(a):'))
#A variável modalidade foi iniciada como uma string vazia, para que depois do teste de múltipla escollha fosse definido seu valor para fins do resultado
  modalidade = ''
#Essa parte do código se refere à definição de qual será o valor da 'modalidade', de acordo com a idade inserida, anteriormente, relacionada à
#própria modalidade de ensino que foi dada com o exercício
  if idade >= 1 and idade <= 5:
    modalidade = 'ensino infantil'
  elif idade >= 6 and idade <=10:
    modalide = 'ensino fundamental I'
  elif idade > 10 and idade < 15:
    modalidade = 'ensino fundamental II'
  elif idade > 15 and idade < 18:
    modalidade = 'ensino médio'
  elif idade > 18:
    modalidade = 'faculdade'
#Primeira informação que retorna ao usuário, confirmando os dados inseridos e o resultado da comparação entre a idade e a modalidade de ensino para 
#assim saber me qual modalide de ensino o aluno será matriculado
  print('O(a) aluno(a) {} de {} anos está no(a) {}' .format(nome, idade, modalidade))
#Agora é requisitado ao usuário novamente que insira um dado, como solicitado, ele deveria escolher entre continuar no programa ou sair.
  escolha=int(input('Deseja continuar: Digite 0 para sim e qualquer outro valor para não'))
#Se a escolha for diferente de 0 o programa é encerrado com a mensagem na tela do usuário
  if escolha != 0:
    print('PROGRAMA ENCERRADO')
#Já se a escolha for exatamente igual a 0, o programa é reiniciado com a função 'matrícula'
  elif escolha == 0:
    matricula()
#O algoritmo se inicia aqui, a função foi definida anteriormente para que essa linha tivesse ação quando iniciado o código. 
#Assim, logo que se desse o ínicio do programa, o algortimo voltaria à primeira linha 
matricula()
