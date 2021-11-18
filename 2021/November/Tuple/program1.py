# Copyright © 2021 Advaith Menon
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of
# this software and associated documentation files (the “Software”), to deal in the
# Software without restriction, including without limitation the rights to use, copy,
# modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""tuple based program

Write a program to input numbers and print the largest and second
largest element of the tuple.
"""

# Import quicksort
# import algorithms
# import algorithms
# sort = algorithms.sorting.quicksort.quicksort
# (or) use Mergesort
# import algorithms
# sort =  algorithms.sorting.merge_sort.mergesort
# (or) builtin function
# sort = list.sort

total = int(input("Enter no of elements: "))
s = []
for _ in range(total):
    s.append(int(input("Enter number {}: ".format(_+1))))

sort(s)
s = tuple(s) # not needed, just because it's tuple chapter
print(s[-1], "is the largest")
print(s[-2], "is second largest")