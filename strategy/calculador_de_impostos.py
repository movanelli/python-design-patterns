from impostos import ISS, ICMS

class Calculador_de_impostos(object):
    def realiza_calculo(self, orcamento, imposto):
        imposto_calculado = imposto.calcula(orcamento)
        print imposto_calculado

if __name__ == '__main__':
    from orcamento import Orcamento

    orcamento = Orcamento(500)

    calculador = Calculador_de_impostos()
    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
