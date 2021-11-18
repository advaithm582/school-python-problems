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

"""tuple program

write program to create mark database
"""
NO_OF_STUDENTS = 5
NO_OF_SUBJECTS = 3

o = []

for i in range(NO_OF_STUDENTS):
    name = input(("|_" if i+1==NO_OF_STUDENTS else\
        "|-") + f"[{i+1}] Name of the Student: ")
    m = []
    for j in range(NO_OF_SUBJECTS):
        m.append(int(input((" " if i+1==NO_OF_STUDENTS else\
        "|") + (f"   |- {name}'s mark in subject {j+1}: "\
            if j+1 != NO_OF_SUBJECTS else \
                f"   |_ {name}'s mark in subject {j+1}: "))))
    o.append(tuple(m))

o = tuple(o)
print(o)