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

"""String With Max Vowels

"""

VOWELS = ('a', 'e', 'i', 'o', 'u')

def count_vowels(string: str) -> int:
    """count_vowels 
    
    Count the vowels in string

    Args:
        string (str): The string

    Returns:
        int: The no. of vowels
    """
    lower_str = string.lower()
    count = int()

    for vowel in VOWELS:
        count += lower_str.count(vowel)

    return count

def swmv(list_of_str: list[str]) -> str:
    """swmv 
    
    String with most vowels

    Args:
        list_of_str (list[str]): List of strings

    Returns:
        str: String with max vowels
    """

    mv = 0
    st = ''

    for stri in list_of_str:
        count = count_vowels(stri)
        if mv<count:
            mv = count
            st = stri

    return st

if __name__=="__main__":
    print("Type strings, ❌ emoji to stop input")

    list_of_str = list()

    while True:
        s = input("Enter string: ")
        if s=="❌":
            break
        else:
            list_of_str.append(s)

    print(f"The string with max vowel:\n{swmv(list_of_str)}")