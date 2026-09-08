d = {}
while True:
    try:
        x = input("")
        if x.lower().strip() in d:
            d[x.lower().strip()] += 1
        else:
            d[x.lower().strip()] = 1
    except EOFError:
        print()
        for palavra, atributo in sorted(d.items()):
            print(f"{atributo} {palavra.upper()}")
        break
