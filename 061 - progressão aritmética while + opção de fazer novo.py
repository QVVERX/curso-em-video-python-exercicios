print('-='*30)
print("               PROGRESSÃO ARITMÉTICA\n               (1O primeiro termos)")
print('-='*30)
res = ''
while res != 'N' and res !='NAO' and res != 'NÃO':
    termo1 = int(input("Primeiro termo: "))
    razao = int(input("Razão: "))
    decimo = termo1 + (10 - 1) * razao


    c = termo1
    while c < decimo:
        print(c, end='')
        print(' ', end='')
        print("-> " if c != '' else '', end='')
        c += razao
    print("FIM")
    print(' ')
    res = str(input('Deseja fazer novamente com outro termo e razão? [S/N]: ')).strip().upper()
    if  res != 'N' and res !='NAO' and res != 'NÃO' and res != 'S' and res != 'SIM':
        while res != 'N' and res !='NAO' and res != 'NÃO' and res != 'S' and res != 'SIM':
            res = str(input('Desculpe, não entendi.\nDeseja fazer novamente com outro termo e razão? [S/N]: ')).strip().upper()

print('Ok. Muito obrigado e volte sempre')