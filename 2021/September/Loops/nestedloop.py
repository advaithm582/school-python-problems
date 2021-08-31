import os
_c = lambda: os.system('cls')

for i in range(0, 101):
    for j in range(0, 101):
        for _ in range(i+1): print("+", " " * (_-2), "+", sep="")
        print("+"*j)
        _c()
        
