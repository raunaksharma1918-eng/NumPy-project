"""
1. Map

Purpose: Apply a function to every item of an iterable (like a list) 
and return a new iterable (map object).

Syntax: map(function, iterable)

Example:"""
# Example: Square numbers
numbers = [1, 2, 3, 4]
squared = map(lambda x: x**2, numbers)
print(list(squared))
# Output: [1, 4, 9, 16]
"""
2. Filter

Purpose: Filter items from an iterable based on a condition.

Syntax: filter(function, iterable)

Example:
"""
# Example: Get even numbers
numbers = [1, 2, 3, 4, 5]
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))
# Output: [2, 4]


"""
3. Zip

Purpose: Combine multiple iterables (lists, tuples, etc.) into pairs of elements.

Syntax: zip(iterable1, iterable2, ...)

Example:"""

# Example: Combine names and ages
names = ['Akarsh', 'Rahul', 'Priya']
ages = [25, 22, 23]
combined = zip(names, ages)
print(list(combined))
# Output: [('Akarsh', 25), ('Rahul', 22), ('Priya', 23)]