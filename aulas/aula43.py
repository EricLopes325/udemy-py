# senha_salva = "123"
# senha_digitada = ''
# repeticoes = 0


# while senha_digitada != senha_salva:
#     senha_digitada = input(f"Sua senha ({repeticoes}x):")

#     repeticoes += 1

# print(repeticoes)
# print("Aquele laço pode ter repetições infinitas!!")

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')