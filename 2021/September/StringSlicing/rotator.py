inp1, inp2 = input(": "), input(": ")

if len(inp1) > len(inp2): _ = inp1; print(inp2)
elif len(inp1) < len(inp2): _=inp2; print(inp1)
else: raise ValueError


if len(_)%2==0: rows,odr = len(_)//2, False
else: rows,odr = len(_)//2+1, True

if not odr:
    f, l = 0, len(_) - 1
    for row in range(rows):
        nsb, nsa = (f), ((len(_)-1)-l) 
        nsm = len(_)-nsb-nsa-2
        print(" "*(nsb+row), _[f], " "*(nsm*2)+" "*2, _[l],sep="")
        f +=1
        l -= 1
else:
    f, l = 0, len(_) - 1
    for row in range(rows):
        nsb, nsa = (f), ((len(_)-1)-l) 
        nsm = len(_)-nsb-nsa-2
        if row == rows-1:
            print(" "*(nsb+row+1), _[f],sep="")
            break
        print(" "*(nsb+row), _[f], " "*(nsm*2)+" "*2, _[l],sep="")
        f +=1
        l -= 1
