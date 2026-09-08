def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    i = 0
    j = 0
    k = 0
    l = 0
    if (len(s) > 6) or (len(s) < 2):
        return False
    for c in s:
        i += 1
        if c.isalpha():
            j +=1
        if (j < 2) and (i == 2):
            return False
        if not (c.isalnum()):
            return False
        if (c.isdigit()):
            l +=1
        if (c == "0") and (l == 1):
            return False
    while k < 6:
        m = k + 1
        if (m < len(s)):
            if (s[k].isdigit()) and (s[m].isalpha()):
                return False
        k += 1
    return True

main()
