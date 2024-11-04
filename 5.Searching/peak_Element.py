def peakElement(arr, n):
    left, right = 0, n - 1

    while left <= right:
        mid = left + (right - left) // 2
        
        # Check if the mid element is a peak
        if (mid == 0 or arr[mid] >= arr[mid - 1]) and (mid == n - 1 or arr[mid] >= arr[mid + 1]):
            return mid
        
        # If the element on the left is greater, then there must be a peak on the left side
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            right = mid - 1
        
        # If the element on the right is greater, then there must be a peak on the right side
        else:
            left = mid + 1

# Example usage
arr = [1, 1, 1, 2, 1, 1, 1]
n = len(arr)
index = peakElement(arr, n)
print("Index of peak element:", index)
