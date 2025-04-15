def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element (here, we choose the last element)
    pivot = arr[-1]
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    
    # Recursively apply quick_sort to the left and right parts
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
