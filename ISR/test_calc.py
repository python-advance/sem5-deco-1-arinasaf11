import unittest
import dec_calc as calc

class CalcTest(unittest.TestCase):
    def test_convert(self):
        self.assertEqual(calc.convert(50), 0.7191988699947355) #из рублей в доллары
        #self.assertEqual(calc.convert(1), 69.5218) #из доллара в рубли
       
if __name__ == '__main__':
    unittest.main()
