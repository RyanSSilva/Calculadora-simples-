

def somar():
    try:

        a=int(input("Qual o primeiro número: "))
        b=int(input("Qual o segundo número: "))
        total=a+b
        print(f"O resultado da operação de {a} + {b} é igual a: {total}")

    except ValueError:
        print("Erro! Digite apenas números!")
    

def sub():
    try:

        a=int(input("Qual o primeiro número: "))
        b=int(input("Qual o segundo número: "))
        total=a-b
        print(f"O resultado da operação de {a} - {b} é igual a: {total}")

    except ValueError:
        print("Erro! Digite apenas números!")
        
    


def div():
    try:
        a=int(input("Qual o primeiro número: "))
        b=int(input("Qual o segundo número: "))
        total=a/b
        print(f"O resultado da operação de {a} dividido por {b} é igual a: {total}")

    except ValueError:
            print("Erro! Digite apenas números!")

def multi():
    try:
        a=int(input("Qual o primeiro número: "))
        b=int(input("Qual o segundo número: "))
        total=a*b
        print(f"O resultado da operação de {a} vezes {b} é igual a: {total}")
        
    except ValueError:
            print("Erro! Digite apenas números!")
    

