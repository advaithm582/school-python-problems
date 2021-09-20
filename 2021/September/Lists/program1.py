"""Bubble Sort

This program sorts a list.
"""
lst = list(map(int, input("Enter any no.of nos: space sep: ").split()))

for j in range(0, len(lst)+1):
   for i in range(0, len(lst)+1):
       # print("ss", i, len(lst))
       if i <= len(lst)-2:
           # print(i)
           # print(lst)
           # print("NOW:",lst[i],lst[i+1])
           if lst[i]>lst[i+1]:
               lst[i], lst[i+1] = lst[i+1], lst[i]
               # print("INTERCHANGED:",lst[i],lst[i+1])

print(lst[-1])