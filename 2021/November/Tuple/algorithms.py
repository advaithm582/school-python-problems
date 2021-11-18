import sys

try:
    open("LICENSE").close()
except:
    sys.path.insert(0, "../../../algorithms/python/")
else:
    sys.path.insert(0, "./algorithms/python/")

import graph
import searching
import sorting