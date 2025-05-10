"""
What is Recursion?
Recursion is when a function calls itself to solve smaller parts of a problem until it reaches a base case — the point where it stops calling itself.

It’s like solving a big puzzle by breaking it into smaller versions of the same puzzle.

Simple Example: Sum of a List
Let's recursively sum the elements of a list (without using loops):
"""

def recursive_sum(lst):
    # Base case: empty list has sum 0
    if not lst:
        return 0
    # Recursive case: first element + sum of the rest
    return lst[0] + recursive_sum(lst[1:])

# Example usage
numbers = [2, 4, 6, 8]
print(recursive_sum(numbers))  # Output: 20
