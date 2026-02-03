#Mostrar o dobro, triplo e raiz quadradada do número lido
num = int(input('Digite um número: '))
dobro = num * 2
triplo = num * 3
raiz = num ** (1/2)
print('O dobro do seu número vale: {} \n O triplo do seu número vale: {} \n A raiz quadrada do seu número vale: {:.2f}'.format(dobro, triplo, raiz))