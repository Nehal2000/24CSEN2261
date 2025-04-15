def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Step 1: Create empty buckets
    bucket_count = 10
    max_value = max(arr)
    min_value = min(arr)
    bucket_range = (max_value - min_value) / bucket_count
    buckets = [[] for _ in range(bucket_count)]

    # Step 2: Put array elements in buckets
    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index == bucket_count:  # for edge case when num == max_value
            index -= 1
        buckets[index].append(num)

    # Step 3: Sort individual buckets and concatenate
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array

# Example usage
arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]
print("Original array:", arr)
sorted_arr = bucket_sort(arr)
print("Sorted array:", sorted_arr)
