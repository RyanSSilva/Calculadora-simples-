print("SEJA BEM VINDO A CALCULADORA")

import funcoes

fluxo = True

while fluxo:

    try:
            operacao=int(input("1 - SOMAR 2 - SUBTRAÇÃO 3 - MULTIPLICAÇÃO 4 - DIVISÃO 5 - ENCERRAR PROGRAMA " \
            "\n QUAL OPERAÇÃO OU OPÇÃO VOCÊ DESEJA: "))
        
            if operacao ==1:
                funcoes.somar()
        
            elif operacao==2:
                funcoes.sub()
        
            elif operacao==3:
                funcoes.multi()
        
            elif operacao==4:
                funcoes.div()
        
            elif operacao==5:
                fluxo=False
                print("PROGRAMA FINALIZADO")
                
        
            else:
                print("OPÇÃO INVALIDA, POR FAVOR ESCOLHA A OPÇÃO CORRETA!")

    except ValueError:
        print("ERRO! Digite números apenas das opções citadas (1 a 5)")
