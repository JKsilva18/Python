# Calcular a área da parede e ver quanto de tinta precisa para pintar
largura = float(input('Qual a largura da parede em metros: '))
comprimento = float(input('Qual a comprimento em metros: '))
area = largura * comprimento
litro = area / 2
print('Para pintar a parede com área {}, necessita de {} litros de tinta'.format(area, litro))