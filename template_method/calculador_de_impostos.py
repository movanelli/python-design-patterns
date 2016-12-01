from impostos import ISS, ICMS, ICPP, IKCV

class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print imposto_calculado

if __name__ == '__main__':
    from orcamento import Orcamento, Item

    orcamento = Orcamento()
    calculador = Calculador_de_impostos()

    orcamento.adiciona_item(Item('Item - 1', 100))
    orcamento.adiciona_item(Item('Item - 2', 50))
    orcamento.adiciona_item(Item('Item - 3', 400))

    print 'ISS e ICMS'
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    print 'ICPP e IKCV'
    calculador.realiza_calculo(orcamento, ICPP())
    calculador.realiza_calculo(orcamento, IKCV())
