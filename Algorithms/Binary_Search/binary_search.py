class BinarySearch:
    """
    Given an array of sorted elements, we find the elements
    based on mid values of the array.
    - If the target is bigger than mid, we reset 'start' to mid + 1
    - If the target is lesser than mid, we reset 'end' to mid - 1
    - If the target is equal to mid, then we return.

    We only check for Half of the array. Hence worst case: O(log n)
    arr = [2, 4, 6, 9, 11, 12, 14, 20, 36, 48]
    """

    def bs_asc_or_desc(self, arr):
        if len(arr) > 0:
            arr_size = len(arr) - 1
            if arr[0] < arr[arr_size]:
                return True
            else:
                return False
        else:
            return None

    def binary_search(self, arr, target):
        # Base case: arr is empty
        if len(arr) == 0:
            return None

        start = 0
        end = len(arr) - 1

        while start <= end:
            # (start + end) // 2 at some point when we do
            # (start + end) might exceed integer limit.
            # Doing start + (end - start) // 2 is optmized way.
            mid = start + (end - start) // 2

            # Order agnoistic Binary Search
            if self.bs_asc_or_desc(arr):
                if target > arr[mid]:
                    start = mid + 1
                elif target < arr[mid]:
                    end = mid - 1
                elif target == arr[mid]:
                    return mid
            else:
                if target > arr[mid]:
                    end = mid - 1
                elif target < arr[mid]:
                    start = mid + 1
                elif target == arr[mid]:
                    return mid
        return None


if __name__ == "__main__":
    # Driver code.
    bs = BinarySearch()
    arr = [-17, -4, 6, 9, 11, 12, 14, 20, 36, 48]
    # arr = [48, 36, 20, 14, 12, 11, 9, 6, -4, -17]
    res = bs.binary_search(arr, 14)

    if res is not None or res == 0:
        print("Element found at index: ", res)
    else:
        print("Element not found.")
