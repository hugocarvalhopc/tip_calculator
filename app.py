print('-' * 40)
print('{:^40}'.format('BEM VINDO AO CALCULADOR DE GORJETAS'))
print('-' * 40)

total_conta = float(input('\nPor favor, informe o total da conta: R$ '))

porcent_gorjeta = int(input('\nMe informe a porcentagem da gorjeta, escolha entre [10], [12] ou [15]: '))

total_pessoas = int(input('\nPor quantas pessoas a conta total será dividida? '))

preco_com_porcent = total_conta + porcent_gorjeta / 100 * total_conta

preco_dividido = preco_com_porcent / total_pessoas

print()
print('-' * 50)
print(f'O preço final para cada um será de {preco_dividido:.0f} reais.')
print('-' * 50)


