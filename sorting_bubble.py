import unittest

def sort(arr): 
    n = len(arr) 

    # Each loop
    # Compare 2 consecutive items
    # If the first item larger than the next item
    # Then swap them
    #
    # Ex:
    # compare (18, 7)
    # return  (7, 18)
    #
    # By doing it for every elements on an array.
    # At the end we will have the largest item swapped
    # at the end of array.
    #
    # Next loop reduces the size of array, until the size
    # equal 1, then we have a sorted array
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]: 
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

    # Analysis
    # T(n) = 1 + 2 + ... + n - 1
    # O(n) = n^2

class BubbleSortTestCase(unittest.TestCase):
    # Given
    # [64, 34, 25, 12, 22, 11, 90]
    #
    # The loops:
    # 1: [34, 25, 12, 22, 11, 64, 90]
    # 2: [25, 12, 22, 11, 34, 64, 90]
    # 3: [12, 22, 11, 25, 34, 64, 90]
    # 4: [12, 11, 22, 25, 34, 64, 90]
    # 5: [11, 12, 22, 25, 34, 64, 90]
    # 6: [11, 12, 22, 25, 34, 64, 90]
    def test(self):
        actual = [64, 34, 25, 12, 22, 11, 90]
        sort(actual)

        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(expected, actual)

unittest.main()
