due = 50
coin = 0
total_amount = 0
while total_amount < 50:
    print(f"Amount due: {due}")
    coin = input("Insert coin: ")
    if (coin != "25") and (coin != "10") and (coin != "5"):
        continue
    else:
        total_amount = total_amount + int(coin)
        if total_amount >= 50:
            change = total_amount - 50
            print(f"Change Owed: {change}")
        due = due - int(coin)

