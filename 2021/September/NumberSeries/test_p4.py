import unittest

def prog4(n):
   s = 2
   fav = 1
   if n == 1:
      s = 1
   else:
      for i in range(3, n+1):
         if i == 100: break
         fav *= (i-1)
         s += (1/fav)
   return s

class P4Test(unittest.TestCase):
   # return True or False
   def test_num_equal(self):
      self.assertTrue(prog4(18) == prog4(30))

# running the test
unittest.main()