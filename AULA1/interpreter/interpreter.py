a = input("Expression: ")
x, y, z = a.strip().split()
x = int(x)
z = int(z)
match y:
    case "+":
        w = x + z
        print(f"{w:.1f}")
    case "-":
        w = x - z
        print(f"{w:.1f}")
    case "/":
        w = x / z
        print(f"{w:.1f}")
    case "*":
        w = x * z
        print(f"{w:.1f}")

