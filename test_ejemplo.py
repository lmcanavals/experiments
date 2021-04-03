from ejemplo import sumar, heapify
import unittest

class TestEjemeplo(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(sumar(5, 6), 11, "debe ser 11")

    def test_heapify(self):
        self.assertEqual(heapify([1, 2, 3, 4]), [4, 2, 3, 1], ":(")

if __name__ == '__main__':
    unittest.main()
