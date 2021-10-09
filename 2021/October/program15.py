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

"""List Operation

Read a list of numbers and display the 1st highest, 2nd highest, 1st least 2nd least number
"""

import program16 as p16

if __name__=="__main__":
    list_2_sort = list()

    while True:
        inp = input("Please enter a number. " "Type EXIT to exit: ")
        if inp.upper() != "EXIT":
            if inp.isdecimal():
                list_2_sort.append(int(inp))
            else:
                print("Grr! I understand only numbers.")
        else:
            break

    sorted_lst = p16.bubble_sort(list_2_sort)

    print(
      f"+------------------------+--------+\n"
      f"| The Largest Number     | {sorted_lst[-1]}\n"
      f"| The 2nd Largest Number | {sorted_lst[-2]}\n"
      f"| The Least Number       | {sorted_lst[1]}\n"
      f"| The 2nd Least Number   | {sorted_lst[2]}\n"
      f"+------------------------+--------+\n")