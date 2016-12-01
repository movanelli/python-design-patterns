# -*- coding: UTF-8 -*-

def imprime(nota_fiscal):
    print 'Imprimindo nota fiscal %s' % (nota_fiscal.cnpj)

def envia_por_email(nota_fiscal):
    print 'Enviando por e-mail a nota fiscal %s' % (nota_fiscal.cnpj)

def salva_no_banco(nota_fiscal):
    print 'Salvando no banco a nota fiscal %s' % (nota_fiscal.cnpj)
