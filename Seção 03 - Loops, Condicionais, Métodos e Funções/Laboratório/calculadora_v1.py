# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

print("Selecione o número da operação desejada:\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão")
opcao = int(input("Digite sua opção (1/2/3/4): "))

number_01 = int(input("Digite o primeiro número: "))
number_02 = int(input("Digite o segundo número: "))


if opcao == 1:
   print(f'{number_01} + {number_02} = {number_01 + number_02}')
elif opcao == 2:
    print(f'{number_01} - {number_02} = {number_01 - number_02}')
elif opcao == 3:
    print(f'{number_01} * {number_02} = {number_01 * number_02}')
elif opcao == 4:
    print(f'{number_01} / {number_02} = {number_01 / number_02}')
else:
    print("Selectione uma das opções válidas")