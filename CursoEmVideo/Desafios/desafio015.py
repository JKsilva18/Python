#Aluguel de carro
dias = int(input('Quantos diárias você pegou?'))
KM = float(input('Quantos KM percorrido?'))
diaria = (dias * 60) + (KM * 0.15)

print('Total a ser pago é R${:.2f}'.format(diaria))