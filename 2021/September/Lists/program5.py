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

import logging
logging.basicConfig(encoding='utf-8', level=logging.DEBUG)


logger = logging.getLogger(__name__)

p = print
r = range
l = list
# Map int input
mii = lambda p: list(map(int, input(p).split()))

m = mii("Enter numbers: ")

ll = l()
rl = l()

fl = l()

for i in r(len(m)):
    logger.debug(f"{m}, {m[i]}, {i}")
    if not m[i]%2:
        # even no
        fl += [m[i]]

for i in r(len(m)-1, -1, -1):
    logger.debug(f"loop 2 {i} {m}")
    logger.debug(f"num {m[i]}")
    if m[i]%2 != 0:
        # if i%2 is not zero
        # list concatenation
        fl = fl[::-1]
        logger.debug(f"num {m[i]}")
        logger.debug(f"rev {fl}")
        fl += [m[i]]
        fl = fl[::-1]
        logger.debug(f"norm {fl}")
        
p(fl)
