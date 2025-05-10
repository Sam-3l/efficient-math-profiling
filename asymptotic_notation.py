"""
📈 Asymptotic Notation Explained
Asymptotic notation describes how the runtime or space of an algorithm grows as the input size n increases.

It ignores constants and low-order terms.

It helps us compare algorithms at scale.

🧠 Big O (O-notation)
O(n) means worst-case time grows linearly with n.

It's used to describe upper bounds on performance.

🧪 Code Snippets for Each Complexity
"""

# O(1) – Constant Time
def get_first_element(arr):
    return arr[0]  # Always 1 step

# O(log n) – Logarithmic Time (Binary Search)
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# O(n) – Linear Time
def linear_search(arr, target):
    for i in arr:
        if i == target:
            return True
    return False

# O(n log n) – Efficient Sort (e.g. Merge Sort)
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    return result + left + right

# O(n^2) – Nested Loops (e.g. Bubble Sort)
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# O(n^k) – Polynomial Time (Example with k=3)
def cubic_time_function(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                pass  # O(n^3) operations
