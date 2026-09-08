d = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}
z = 0
while True:
    try:
        x = input("Item: ")
        if x.lower() in d:
            z += d[x.lower()]
            print(f"Total: ${z:.2f}")
    except EOFError:
        break
