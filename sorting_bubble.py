import unittest

def sort(arr): 
    n = len(arr) 

    for i in range(n-1):
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

class BubbleSortTestCase(unittest.TestCase):
    def test(self):
        actual = [64, 34, 25, 12, 22, 11, 90]
        sort(actual)

        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(expected, actual)

unittest.main()
