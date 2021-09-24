"""Bubble Sort"""

import logging


logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


logger = logging.getLogger(__name__)

p = print
r = range
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

p(lst)
        
