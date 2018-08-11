#progressão aritmetica

primeiro = int(input("Digite o primeiro termo: "))
razao = int(input("digite o razão: "))
decimo = primeiro + (10 - 1) * razao
cont = 0
while cont < decimo:
  
  cont = cont + razao
  print(" {} ".format(cont), end='')

