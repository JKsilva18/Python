n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
res = n1 % n2
sub = n1 - n2

print('A soma vale: {}, \n a multiplicação vale: {}, \n a divisão vale: {:.3f}, \n a divisão inteira vale: {}, \n a potencia vale: {}, \n o resto da divisão vale: {}, \n a subtração vale: {}'.format(s, m, d, di, e, res, sub))