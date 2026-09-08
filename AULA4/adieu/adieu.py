import inflect
p = inflect.engine()
lista =[]

while True:
        try:
            x = input("Name: ")
            lista.append(x)
        except EOFError:
             print()
             print(f"Adieu, adieu, to {p.join(lista)}")
             break


