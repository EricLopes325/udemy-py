"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = int(input("Digite um número inteiro: "))

# if numero % 2 == 0:
#     print(f"O número {numero} é par")               # MEU CODE
# else:
#     print(f"O número {numero} é impar")


# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'             

#     if par_impar:                                     #CODE PROFESSOR
#         par_impar_texto = 'par'

#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você não digitou um número inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input("Digite a hora em numeros inteiros: ")
# try:
#     hora = int(entrada)

#     if hora >= 0 and hora <= 11:
#         input("Bom dia")
#     elif hora >= 12 and hora <= 17:
#         print("Boa tarde")                        #Meu code
#     elif hora >= 18 and hora <= 23:
#         print("Boa noite")
#     else:
#         print("Não conheço esta hora")
# except:
#     print("por favor, digite números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input("Qual seu nome: ")

# tamanho_nome = len(nome)

# if tamanho_nome >1:
#     if tamanho_nome <= 4:
#         print("Seu nome é curto")
#     if tamanho_nome >= 5 and tamanho_nome <= 6:       #MEU CODE COM ALGUMAS ALTERAÇÕES DO PROF
#         print ("Seu nome é normal")
#     else:
#         print("Seu nome é grande")
# else:
#     print("Digite mais de uma letra")