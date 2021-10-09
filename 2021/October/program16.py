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

"""Sort a list"""

import logging
import typing as t


logger = logging.getLogger(__name__)


def is_number(item: t.Any) -> bool:
    """is_number 
    
    is item a comparable number

    Args:
        item (Any): The item

    Returns:
        bool: Whether it's no or not
    """
    if type(item) == int or type(item) == str:
        print(type(item))
        return True
    else:
        return False


def bubble_sort(list_):
    """bubble_sort 
    
    Bubble Sort Algorithm

    Args:
        list_ (list): The list to be sorted

    Returns:
        list: Sorted list
    """
    lst = list_[:]
    logger.debug(f"list {lst}")

    for pass_no in range(1, len(lst)+1):
        logger.debug(f"Pass no {pass_no}")
        for i in range(len(lst)-pass_no):
            logger.debug(f"i {i}")
            logger.debug(f"{lst[i]} and {lst[i+1]}")

            if not (is_number(lst[i]) and is_number(lst[i+1])):
                raise ValueError("Uncomparable Datatypes")

            if lst[i]>lst[i+1]:
                logger.debug(f"switched")
                lst[i], lst[i+1] = lst[i+1], lst[i]
                logger.debug(f"after: {lst[i]} and {lst[i+1]}")
            logger.debug(f"After operation: {lst}")
            logger.debug(f"----------------------")
        logger.debug(f"Pass {pass_no} has ended")
        logger.debug(f"=============END PASS {pass_no}=============")

    return lst


if __name__=="__main__":
    logging.basicConfig(encoding='utf-8', level=logging.DEBUG)