while True:
    try:
        x = input("Fraction: ")
        x, y = x.split("/")
        z = (float(x)/float(y)) * 100
        z = round(z)
        if (z >= 99) & (z <= 100):
            print("F")
        elif (z > 100) or (int(x) < 0) or (int(y) < 0):
            a = int(x)/0
        elif z <= 1:
            print("E")
        else:
            print(f"{int(z)}%")
        break
    except (ValueError, ZeroDivisionError):
        pass
