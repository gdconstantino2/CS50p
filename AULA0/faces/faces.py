def convert(msg1):
    msg1 = msg1.replace(":)","🙂")
    msg1 = msg1.replace(":(","🙁")
    return msg1
def main():
    msg = input()
    msg2 = convert(msg)
    print(msg2)
main()
