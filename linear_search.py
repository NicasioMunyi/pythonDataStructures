def linear_search(list, target):
    """
    Returns the index position of the target if found, else None.
    """
    for i in range(0, len(list)):  # Iterate through each element in the list
        if list[i] == target:  # If the current element matches the target
            return i  # Return the index of the target
    return None  # Return None if target is not found


def verify(index):
    if index is not None:  # If index is not None, target is found
        print("Target found at index", index)  # Print the index of the target
    else:  # If index is None, target is not found
        print("Target not found in the list")  # Print a message indicating target not found

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = linear_search(numbers, 10)  # Perform linear search for target 10
verify(result)  # Verify the result of the linear search
