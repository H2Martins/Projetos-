continuar_usando = "SIM"

while continuar_usando == "SIM":
  
 #Criando um menu de opções
  print("SELECIONE A OPERAÇÃO DESEJADA")
  print("1 para Correção com 1 Teor")
  print("2 para Correção com 2 Teores")
  print("3 para Correção com 3 Teores")

  # Interação com o usuário

  operacao = input('\nQual operação você deseja realizar? :')

  #Criando as operações e as apresentações de respostas

   #1TEOR 
  if operacao == '1':
    print('*CALCULO COM 1 TEOR*')
    qtd100 = float(input("\nDigite a quantidade que devera ser utilizada a 100%: "))
    teor = float(input("Digite seu Teor: "))
    d1 = float(100)
    while teor == 0:                  #Garantindo que d2 não seja zero!! 
     print("O segundo valor não pode ser zero!")
     teor = float(input("\nDigite o Teor novamente! (diferente de zero): "))
    divisao = qtd100 / teor
    res = round((divisao * d1),3)
    print("\nQuantidade a ser usada é:{}""\n".format(res))
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

    #2TEORES
  if operacao == '2':
    print('*CALCULO COM 2 TEORES*')
    qtd100 = float(input("\nDigite a quantidade que devera ser utilizada a 100%: "))
    qtdFr = float(input('\nInforme quantidade fisica restante: '))
    teorFr = float(input("\nDigite o Teor da quantidade fisica restante: "))
    d2 = float(100)
    nTeor = float(input('Digite o novo teor: '))
    while qtdFr == 0:                  #Garantindo que d2 não seja zero!! 
      print("O segundo valor não pode ser zero!")
      qtdFr = float(input("\nDigite o segundo valor (diferente de zero): "))
    while nTeor == 0:                  #Garantindo que d2 não seja zero!! 
      print("O segundo valor não pode ser zero!")
      nTeor = float(input("\nDigite o segundo valor (diferente de zero): "))
    mult = round(((qtdFr * teorFr) / d2), 3)
    res0 = round((qtd100 - mult), 3)
    res1 = round((res0 / nTeor * d2 + qtdFr), 3)
    print("\nQuantidade a ser utilizada é:{}""\n".format(res1))
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")

    #3TEORES
  if operacao == '3':
    print('*CALCULO COM 3 TEORES*')
    qtd100 = float(input("\nDigite a quantidade que devera ser utilizada a 100%: "))
    qtdFr1 = float(input('\nInforme Primeira quantidade fisica restante: '))
    teorFr1 = float(input('\nDigite o Teor da Primeira quantidade fisica restante: '))
    qtdFr2 = float(input("\nInforme Segunda quantidade fisica restante: "))
    teorFr2 = float(input('\nDigite o Teor da Segunda quantidade fisica restante: '))
    nTeor = float(input('\nDigite o Novo Teor: '))
    d3 = float(100)
    while qtdFr1 == 0:                  #Garantindo que d2 não seja zero!! 
      print("O segundo valor não pode ser zero!")
      qtdFr1 = float(input("\nDigite o segundo valor (diferente de zero): "))
    while nTeor == 0:              #Garantindo que d2 não seja zero!! 
      print("O segundo valor não pode ser zero!")
      nTeor = float(input("\nDigite o segundo valor (diferente de zero): "))
    mult = round(((qtdFr1 * teorFr1) / d3), 3)
    mult2 = round(((qtdFr2 * teorFr2) / d3), 3)
    res0 = round((qtd100 - mult - mult2), 3)
    res1 = round((res0 / nTeor * d3 +qtdFr1 +qtdFr2 ), 3)
    print("\nQuantidade a ser utilizada é:{}""\n".format(res1))
    print("*"*33,"\n")
    continuar_usando = input("Gostaria de fazer outra operação? ").upper()
    print("*"*33,"\n")
