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

"""tuple problems

Write a program to check if elements in the first half of a tuple are 
sorted in ascending order.
"""

# For this algorithm we can use QuickSort
import algorithms
sort = algorithms.sorting.quicksort.quicksort
# Not recommended:
# (or) use Mergesort
# import algorithms
# sort =  algorithms.sorting.merge_sort.mergesort
# (or) builtin function
# sort = list.sort # mergesort+insertion sort
# All algorithms has O(n log n), so that's cool
# But bubble sort has O(n^2), and that is NOT COOL.

tup = input("Enter a tuple: ")
tup = eval(tup if tup.replace(",","").isdigit() else "exit()")
lst = list(tup)
sort(lst,r=len(lst)//2)
# or
# sort(lst)
tups = tuple(lst)
print("yes" if tups[:len(lst)//2+1] == tup[:len(lst)//2+1] else "no")

