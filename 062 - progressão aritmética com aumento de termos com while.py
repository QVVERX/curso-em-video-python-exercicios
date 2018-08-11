print('-='*30)
print("               PROGRESSÃO ARITMÉTICA\n               (1O primeiro termos)")
print('-='*30)

termo1 = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

total = 0
mais = 10

c = termo1

while mais != 0:
    total = total + mais
    decimo = termo1 + (total - 1) * razao
    while c < decimo:
        print(c, " -> ",  end= '')
        c += razao
    print(" PAUSA")
    mais = int(input("Quantos termos você quer a mais:\n(Caso seja 0, o programa será finalizado): "))
    c = 0
print("Muito obrigado e volte sempre!")