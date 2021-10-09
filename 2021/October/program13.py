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

"""Capitalize each word

Read a string and capitalize 1st letter of every word.
Avoid builtins.
"""
def capitalize_word(string):
    """capitalize_word 
    
    Title case the word without .title

    Args:
        string (str): The string

    Returns:
        str: The capitalized string
    """
    final_word = str()

    # #1 - Split the string
    split_str = string.split()

    # #2 - For each word, captialise
    for word in split_str:
        ascii_word = ord(word[0])
        if 97<=ascii_word<=122:
            # it is a small letter
            cap_let = chr(ascii_word-32)
            final_word += cap_let + word[1:] + " "
        else:
            final_word += word + " "

    # #3 - Get rid of space
    final_word = final_word[:-1]

    return final_word

if __name__=="__main__":
    s = input("string: ")

    print("Capitalised string: {}".format(capitalize_word(s)))