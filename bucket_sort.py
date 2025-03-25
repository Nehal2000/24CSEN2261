def bucket_sort(arr):
    # Step 1: Find the minimum and maximum elements in the array
    min_val = min(arr)
    max_val = max(arr)
    
    # Step 2: Create an empty list of buckets
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]
    
    # Step 3: Place elements into their respective buckets
    for num in arr:
        index = int((num - min_val) / (max_val - min_val) * (bucket_count - 1))
        buckets[index].append(num)
    
    # Step 4: Sort each bucket and concatenate the result
    return [num for bucket in buckets for num in sorted(bucket)]

# Example usage
arr = [0.42, 0.32, 0.24, 0.51, 0.43, 0.99, 0.58]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
