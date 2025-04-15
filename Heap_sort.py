def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is larger than the root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is larger than the root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from the heap one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max element) with last element
        heapify(arr, i, 0)  # Heapify the root again

# Example usage:
arr = [38, 27, 43, 3, 9, 82, 10]
heap_sort(arr)
print("Sorted array:", arr)
