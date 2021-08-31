for i in range(int(input("no:"))):
    if i%5 == 0: continue
    print(i, "No not divisible by 5")
    if i%13 == 0:
        print("OMG! The prog will crash!")
        break

