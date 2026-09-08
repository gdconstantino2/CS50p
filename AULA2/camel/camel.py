x = input("camelCase: ")
for letra in x:
    if (letra.isupper()):
        x = x.replace(letra, "_" + chr(ord(letra) + 32))
print(x)

