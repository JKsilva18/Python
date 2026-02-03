# Ler um número em metros e converter em centimetros e milimetros
num = int(input('Digite um número: '))
cm = num * 100
mm = num * 1000
print('Seu número em metros é: {} \n Seu número em centimetros é: {} \n Seu número em milimetros é: {}'.format(num, cm, mm))