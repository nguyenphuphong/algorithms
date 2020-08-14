import unittest

def sort(arr): 
    n = len(arr)

    # Each loop
    # Take an item in array
    # Then trace back to the first item
    # Find the correct place to insert that item to array
    for i in range(1, n - 1):
        value = arr[i]
        j = i

        while j > 0 and arr[j - 1] > value:
            arr[j] = arr[j - 1]
            j = j - 1

        arr[j] = value
        print(arr)

    # Analysis
    # T(n) = 1 + 2 + 3 + ... + n -1
    # O(n) = n^2

class InsertionSortTestCase(unittest.TestCase):
    # Given
    # [64, 34, 25, 12, 22, 11, 90]
    # 
    # The loops:
    #
    # 1: [34, 64, 25, 12, 22, 11, 90]
    # 2: [25, 34, 64, 12, 22, 11, 90]
    # 3: [12, 25, 34, 64, 22, 11, 90]
    # 4: [11, 12, 22, 25, 34, 64, 90]
    # 5: [11, 12, 22, 25, 34, 64, 90]
    def test(self):
        actual = [64, 34, 25, 12, 22, 11, 90]
        sort(actual)

        expected = [11, 12, 22, 25, 34, 64, 90]
        self.assertEqual(expected, actual)

unittest.main()
