vowels = ['a', 'e', 'i', 'o', 'u']
x = input("Input: ")
x_copy = x
for c in x:
    for y in vowels:
        if c.lower() == y:
            x_copy = x_copy.replace(c, "")
print(f"Output: {x_copy}")
