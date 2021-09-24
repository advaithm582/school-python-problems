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
"""Bubble Sort"""

import logging


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


logger = logging.getLogger(__name__)

p = print
r = range
i = input
# Range from 1
r1 = lambda stop: range(1, stop+1)
# Range from 1 for iterable
ri = lambda iterable: range(1, len(iterable)+1)
# Map float input
mfi = lambda p: list(map(float, input(p).split()))


lst = mfi("Enter number: ")
logger.debug(f"list {lst}")

for pass_no in ri(lst):
    logger.debug(f"Pass no {pass_no}")
    for i in r(len(lst)-pass_no):
        logger.debug(f"i {i}")
        logger.debug(f"{lst[i]} and {lst[i+1]}")
        if lst[i]>lst[i+1]:
            logger.debug(f"switched")
            lst[i], lst[i+1] = lst[i+1], lst[i]
            logger.debug(f"after: {lst[i]} and {lst[i+1]}")
        logger.debug(f"After operation: {lst}")
        logger.debug(f"----------------------")
    logger.debug(f"Pass {pass_no} has ended")
    logger.debug(f"=============END PASS {pass_no}=============")

p(lst)
        
