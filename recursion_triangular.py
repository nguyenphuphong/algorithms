import unittest

# Triangular numbers: 1, 3, 6, 10, 15, 21, ...
# f(1) = 1
# f(n) = f(n - 1) + n
def triangular(n):
    if n == 1:
        return 1
    return triangular(n - 1) + n

class TriangularRecursionTest(unittest.TestCase):
    def test(self):
        self.assertEqual(6, triangular(3))
        self.assertEqual(15, triangular(5))
        self.assertEqual(21, triangular(6))

unittest.main()
