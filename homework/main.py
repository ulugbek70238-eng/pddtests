# def check_positive(x,y):
#     assert x>0 or y>0
#     return x,y
# print(check_positive(2,1))
# print(check_positive(-2,1))
# print(check_positive(2,1))
import unittest


def product(a, b):
    return a * b

def number_product(a, b):
    if a > b:
        return True
    elif a < b:
        return False

class Test_Numbers(unittest.TestCase):
    def test_product(self):
        self.assertEqual(product(1, 2), 3), 'Можно умножать только числа!'
    def test_product_2(self)
        self.assertEqual(product('Hellow', 1), 8, 'можно умножать только на числа!')
    def test_product_3(self):
        self.assertEqual(product(5,1), True, 'Можно сравнивать только числа!')
    def test_product_4(self):
        self.assertEqual(product('hello','bye'), True, 'можно сравнивать только числа')