amount = int(input("Please Enter amount students : "))
while True:
    if amount <= 5 and amount >= 2:
        records = []
        for i in range(amount):
            name = (input("Enter students name : "))
            score = (float(input("Enter students score : ")))
            records.append([name, score])
            dic = dict(records)
            lowest = min(dic, key=dic.get)
            lowest_value = min(dic.values())
            final = [key for key, value in dic.items() if value ==
                     lowest_value]
        print(sorted(final))
        break
    else:
        print("noooo")
        amount = int(input("Please Enter amount students : "))
