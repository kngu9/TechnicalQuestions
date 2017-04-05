# Given a sorted array, find the number using binary search
# Time Complexity: O(logn)
# Space Complexity: O(1)

def binarySearch(arr, target):
    lo = 1
    hi = len(arr)

    while lo <= hi:
        mid = lo + (hi - lo)/2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1

    return -1

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    index = binarySearch(arr, 7)

    print(index)
