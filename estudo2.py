print('Bem vindo ao seu Banco')
saldo=0

while True:
    try:
     valor_depositado=float(input('Digite o valor a ser depositado:'))
     saldo+=valor_depositado
     print(f'O valor depositado foi de {valor_depositado} reais.')
     print(f'Seu saldo em conta é de {saldo} reais')
    except ValueError:
       print('Tente novamente, Digite apenas valores númericos')
       continue
    repetir=input('Você deseja repetir ? (s/n):').lower()
    if repetir != 's':
       break

print(f'Obrigado, o valor em conta é de {saldo} reais. ')
    

   
   
   

