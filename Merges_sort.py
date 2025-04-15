def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Find the middle point of the array
    mid = len(arr) // 2

    # Recursively split the array into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Merge the two halves in sorted order
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Merge the two sorted lists
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from both halves
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
