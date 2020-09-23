import unittest
from errores.error import ValueNegativeError
from ejercicios.ejercicio1 import factorial

class FactorialTest(unittest.TestCase):
  def testFactorialFromLessOne(self):
    self.assertRaises(ValueNegativeError, factorial,-1)

  def testFactorialFrom0(self):
    result= factorial(0)
    self.assertEqual(1,result)


if __name__ == "__main__":
  unittest.main()
