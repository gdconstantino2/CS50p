from random import randint

def main():
    level = get_level()
    outscore = 0
    for j in range(10):
        i = 0
        x = generate_integer(level)
        y = generate_integer(level)
        z = int(x) + int(y)
        while i < 3:
                try:
                    guess = input(f"{x} + {y} = ")
                    if (int(guess) == z):
                        i = 3
                        outscore += 1
                    else:
                        print("EEE")
                        i += 1
                        if i == 3:
                            print(f"{x} + {y} = {z}")

                except ValueError:
                    print("EEE")
                    i +=1
                    if i == 3:
                        print(f"{x} + {y} = {z}")
                    pass
        j += 1
    print(f"Score: {outscore}")

def get_level():
    while True:
        try:
            level = input("Level: ")
            if level.isalpha() or (int(level) < 1) or (int(level) > 3):
                pass
            else:
                return int(level)
        except ValueError:
            pass


def generate_integer(level):
        if level == 1:
            x = randint(0, 9)
        elif level == 2:
            x = randint(10, 99)
        else:
            x = randint(100, 999)
        return x

if __name__ == "__main__":
    main()
