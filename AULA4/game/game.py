from random import randrange

while True:
    try:
        level = input("Level: ")
        if level.isinstance(level, int):
            x = randrange(1, level)
            n = input("Guess:" )
            if n == x:
                print("Just right!")
            if n < x:
                
    except:
