import unittest
from ejercicios.numero_romano import NumeroRomano

class NumerosRomanosTest(unittest.TestCase):
  def setUp(self):
    self.numeroRomano = NumeroRomano()
  
  def testUnNumeroRomano(self):
    numeroRomano=self.numeroRomano.numeroARomano(1)
    self.assertEqual("I",numeroRomano)
  
  def testDosNumeroRomano(self):
    numeroRomano=self.numeroRomano.numeroARomano(2)
    self.assertEqual("II",numeroRomano)
  
  def testTresNumeroRomano(self):
    numeroRomano=self.numeroRomano.numeroARomano(3)
    self.assertEqual("III",numeroRomano)

  def testCuatroNumeroRomano(self):
    numeroRomano=self.numeroRomano.numeroARomano(4)
    self.assertEqual("IV",numeroRomano)  

  def testCincoNumeroRomano(self):
    numeroRomano=self.numeroRomano.numeroARomano(5)
    self.assertEqual("V",numeroRomano)      

  def testSeisNumeroRomano(self):
    numeroRomano=self.numeroRomano.numeroARomano(6)
    self.assertEqual("VI",numeroRomano)      