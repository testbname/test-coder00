def bubble_sort(arr):
    """
    Sorts an array using the bubble sort algorithm.

    Args:
        arr: A list of comparable elements.

    Returns:
        A new list containing the elements of arr in ascending order.
    """
    # Create a copy to avoid modifying the original list
    sorted_arr = arr.copy()
    n = len(sorted_arr)

    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize: if no swaps occur, the list is sorted
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                swapped = True
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return sorted_arr

# Example usage
if __name__ == "__main__":
    example_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original list: {example_list}")
    sorted_list = bubble_sort(example_list)
    print(f"Sorted list: {sorted_list}")