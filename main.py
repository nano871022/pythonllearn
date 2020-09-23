import unittest

class ValueNegativeError(Exception):
  pass

def factorial(n):
  if n < 0:
    raise ValueNegativeError("Valor negativo no permitido")
  if n == 0 or n == 1:
    return 1
  return n * factorial(n-1)

class FactorialTest(unittest.TestCase):
  def testFactorialFromLessOne(self):
    self.assertRaises(ValueNegativeError, factorial,-1)

  def testFactorialFrom0(self):
    result= factorial(0)
    self.assertEqual(1,result)

if __name__ == "__main__":
  unittest.main()
