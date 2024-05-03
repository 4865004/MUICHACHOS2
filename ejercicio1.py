print("-------------------\n----PIZZERIA PF----\n-------------------\n")
dinero = int(input("Hey chamo cuanta platica ustede carga?"))
ingredientes = []
pizza1 = 30
pizza2 = 40 
pizza3 = 60
precioExtraDeQuesito = 10
if dinero > pizza3:
    pizzaElegida = int(input(f"Hey chamo te ofresco estas 3 pizzas \n pizza1 peperoni => {pizza1}\n pizza2 hawuahiana => {pizza2}\n pizza3 rectanculo => {pizza3}\n hey chamo elige entre 1, 2 o 3\n"))
    if pizzaElegida == 1:
        print("Ey chamo llebas 30 pesitos\n")
        ingredienteExtra = int(input("Hey chamo por 10 pesitos quieres quesito extra\n pon 0 o 1"))
        if ingredienteExtra == 1:
            pizza1 += 10
            print(f"Ey chamo llebas {pizza1} \n")
            quiereSeguir = int(input("Hey Quieres seguir?\n Pon 0 si no y 1 si si\n"))
            if quiereSeguir == 1:
                print("aqui esta tu pizza, come muerto de hambre")
            else:
                print("Vayase a la mierda pe")
        else:
            print("Ok chamo, llega tu pizza sin quesillo")
    elif pizzaElegida == 2:
        print("Ey chamo llebas 40 pesitos\n")
        ingredienteExtra = int(input("Hey chamo por 10 pesitos quieres quesito extra\n pon 0 o 1"))
        if ingredienteExtra == 1:
            pizza2 += 10
            print(f"Ey chamo llebas {pizza2} \n")
            quiereSeguir = int(input("Hey Quieres seguir?\n Pon 0 si no y 1 si si\n"))
            if quiereSeguir == 1:
                print("aqui esta tu pizza, come muerto de hambre")
            else:
                print("Vayase a la mierda pe")
        else:
            print("ok chamo aqui esta su pizza sin quesillo")
    elif pizzaElegida == 3:
        print("Ey chamo llebas 60 pesitos\n")
        ingredienteExtra = int(input("Hey chamo por 10 pesitos quieres quesito extra\n pon 0 o 1"))
        if ingredienteExtra == 1:
            pizza3 += 10
            print(f"Ey chamo llebas {pizza3} \n")
            quiereSeguir = int(input("Hey Quieres seguir?\n Pon 0 si no y 1 si si\n"))
            if quiereSeguir == 1:
                print("aqui esta tu pizza, come muerto de hambre")
            else:
                print("Vayase a la mierda pe")
        else:
            print("ok chamo aqui esta su pizza sin quesillo")
    else:
        print("Vete ala mierda mejor, si solo vienes hacer tus pendejadas")
elif dinero < pizza1:
    print("K uvo parse, losiento pero eres demasiado pobre para comprar una pizza")
else:
    print("losiento chamo no aceptamos dinero alienigena")
