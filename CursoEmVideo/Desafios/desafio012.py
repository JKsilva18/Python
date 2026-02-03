# Ler o preço do produto e aplicar o desconto
preco = float(input('Digite o valor do produto: '))
liquidacao = preco - (preco * 5 / 100)
print('O preço do produto original é: R$ {} \n Na liquidação vale R$ {}'.format(preco, liquidacao))