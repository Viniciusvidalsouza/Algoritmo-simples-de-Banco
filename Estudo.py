print('BEM VINDO AO SEU BANCO')
while True:
      valor_depositado= (input('Digite o valor que vai ser depositado: '))
      try:
        conversao= int(valor_depositado) 
        print(f'O valor de {conversao} reais foi depositado com sucesso.')
        break
      except ValueError:
        print('Valor incorreto, digite valor númerico')

saldo= valor_depositado
saldo_em_conta= saldo

print(f'Seu saldo em conta é {saldo_em_conta} reais.')

