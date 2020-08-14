import unittest

def sort(arr): 
    n = len(arr) 

    # Each loop
    # Find the min value of the array
    # Then swap that value to the first element
    # Ex:
    # (17, 13, 1, 5) -> (1, 13, 17, 5)
    #
    # Next loop reduces the size of array, until the size
    # equal 1, then we have a sorted array
    for i in range(n-1):
        min = i
        for j in range(min + 1, n-1): 
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
        print(arr)
    
    # Analysis
    # T(n) = 1 + 2 + ... + n - 1
    # => O(n) = n^2

class SelectionSortTest(unittest.TestCase):
    # Given
    # [64, 34, 25, 12, 22, 11, 90]
    # 
    # The loops:
    # 1: [11, 34, 25, 12, 22, 64, 90]
    # 2: [11, 12, 25, 34, 22, 64, 90]
    # 3: [11, 12, 22, 34, 25, 64, 90]
    # 4: [11, 12, 22, 25, 34, 64, 90]
    # 5: [11, 12, 22, 25, 34, 64, 90]
    # 6: [11, 12, 22, 25, 34, 64, 90]
    def test(self):
        actual = [64, 34, 25, 12, 22, 11, 90]
        sort(actual)

        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(expected, actual)

unittest.main()
