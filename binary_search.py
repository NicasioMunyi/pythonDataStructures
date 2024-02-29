# Function to perform binary search on a sorted list
def binary_search(list, target):
    first = 0  # Index of the first element in the list
    last = len(list) - 1  # Index of the last element in the list

    # Loop until the search space is exhausted
    while(first <= last):
        midpoint = (first + last) // 2  # Calculate the midpoint index
        if list[midpoint] == target:  # If the target is found at the midpoint
            return midpoint  # Return the index of the target
        elif list[midpoint] < target:  # If the target is greater, search the right half
            first = midpoint + 1  # Update the starting index
        else:  # If the target is smaller, search the left half
            last = midpoint - 1  # Update the ending index

    return None  # If target is not found, return None

# Function to verify the result of binary search
def verify(index):
    if index is not None:  # If index is not None, target is found
        print(f"Element Found at {index}")  # Print the index of the target
    else:  # If index is None, target is not found
        print("Target not found in the list")  # Print a message indicating target not found

# Test list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Perform binary search on the test list for target 10
result = binary_search(numbers, 10)

# Verify the result of binary search
verify(result)


