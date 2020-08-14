import unittest

# Factorial numbers: 1, 2, 6, 24, 120, 720, ...
# f(1) = 1
# f(n) = f(n - 1)*n
def factorial(n):
    if n == 1:
        return 1
    return factorial(n - 1) * n

class TriangularRecursionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(6, factorial(3))
        self.assertEqual(120, factorial(5))
        self.assertEqual(720, factorial(6))

unittest.main()
