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

"""Sum of Numbers and Average

Print the sum of a numbers for a given range,
and find the average of them using loop
"""

__version__ = '0.1.0'
__author__ = 'Advaith Menon'

# INTeger inPUT (INTPUT)
intput = lambda prompt: int(input(prompt))

# AP: Sum 
sum_n = lambda a, l, n: (a+l)*(n/2)

first_term = intput("Enter A: ")
last_term = intput("Enter L: ")
no_of_terms = (last_term-first_term)+1

print("Sum to n terms:", sum_n(first_term, last_term, no_of_terms))
print("Sum to n terms:", sum_n(first_term, last_term, no_of_terms)/no_of_terms)