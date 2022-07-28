import unittest
from poseidon.cpu import ALU


OPCODES = {
          0b00: 'ADD', 
          0b01: 'SUB', 
          0b10: 'MUL',
          0b11: 'DIV'
          }
FLAGS =   {
          'OVERFLOW': False, 
          'ZERO': False,
          'NEGATIVE': False
         }

class TestALU(unittest.TestCase):

  a = ALU(OPCODES, FLAGS)

  def test_add(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010
    self.assertEqual(self.a.ADD(A,B), 13)
 
  def test_sub(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010
    self.assertEqual(self.a.SUB(A,B), 9)
       
  def test_mul(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010
    self.assertEqual(self.a.MUL(A,B), 22)
  
  def test_div(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010
    self.assertEqual(self.a.DIV(A,B), 5)
             
  def test_exec_add(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010

    res, flags = self.a.exec(0b00, A,B)
    self.a.reset()

    self.assertEqual(res, 13)
    self.assertFalse(flags['OVERFLOW'])
    self.assertFalse(flags['ZERO'])
    self.assertFalse(flags['NEGATIVE'])

  def test_exec_sub(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010

    res, flags = self.a.exec(0b01, A,B)
    self.a.reset()

    self.assertEqual(res, 9)
    self.assertFalse(flags['OVERFLOW'])
    self.assertFalse(flags['ZERO'])
    self.assertFalse(flags['NEGATIVE'])


  def test_exec_mul(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010

    res, flags = self.a.exec(0b10, A,B)
    self.a.reset()

    self.assertEqual(res, 22)
    self.assertFalse(flags['OVERFLOW'])
    self.assertFalse(flags['ZERO'])
    self.assertFalse(flags['NEGATIVE'])

  def test_exec_div(self):
    A: BYTE = 0b00001011
    B: BYTE = 0b00000010

    res, flags = self.a.exec(0b11, A,B)
    self.assertEqual(res, 5)
    self.assertFalse(flags['OVERFLOW'])
    self.assertFalse(flags['ZERO'])
    self.assertFalse(flags['NEGATIVE'])

    self.a.reset()

  def test_flag_overflow(self):
    A: BYTE = 0b11111111
    B: BYTE = 0b00000001

    res, flags = self.a.exec(0b00, A,B)
    self.assertEqual(res, 256)
    self.assertTrue(flags['OVERFLOW'])
    self.assertFalse(flags['ZERO'])
    self.assertFalse(flags['NEGATIVE'])

    self.a.reset()

  def test_flag_zero(self):
    A: BYTE = 0b00000000
    B: BYTE = 0b00000000

    # 0 + 0 = 0
    res, flags = self.a.exec(0b00, A,B)
    self.assertEqual(res, 0)
    self.assertFalse(flags['OVERFLOW'])
    self.assertTrue(flags['ZERO'])
    self.assertFalse(flags['NEGATIVE'])

    self.a.reset()

    # 8 * 0 = 0
    A: BYTE = 0b00001000

    res, flags = self.a.exec(0b10, A,B)
    self.assertEqual(res, 0)
    self.assertFalse(flags['OVERFLOW'])
    self.assertTrue(flags['ZERO'])
    self.assertFalse(flags['NEGATIVE'])

    self.a.reset()

  def test_flag_negative(self):
    A: BYTE = 0b00000010
    B: BYTE = 0b00001011

    res, flags = self.a.exec(0b01, A,B)
    self.assertEqual(res, -9)
    self.assertFalse(flags['OVERFLOW'])
    self.assertFalse(flags['ZERO'])
    self.assertTrue(flags['NEGATIVE'])

    self.a.reset()

if __name__ == '__main__':
  unittest.main(verbosity=2)