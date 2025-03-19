"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""

contador = 0 

while contador <= 40:
        contador += 1

        if contador == 8:
            print("Não irei mostrar o número", contador)
            continue

        if contador >= 10 and contador <= 28:
            print("Não irei mostrar o número", contador)
            continue

        print(contador)

        if contador >= 40:
            break
           