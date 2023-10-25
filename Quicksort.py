def quicksort(arr):
    """
    This function performs a quicksort on a list of numbers.

    Parameters:
    arr (list of ints): The list to sort.

    Returns:
    list of ints: The sorted list.
    """
    if len(arr) <= 1:
        # Base case: a list of zero or one elements is already sorted
        return arr
    else:
        # Choosing the pivot: the element that will be in its final sorted position
        # For simplicity, we choose the last element in the list, but there are other methods.
        pivot = arr[-1]
        smaller, equal, larger = [], [], []
        for num in arr:
            # Divide the list into three categories
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)

        # Conquer: Recursively apply quicksort to the smaller and larger lists
        return quicksort(smaller) + equal + quicksort(larger)

# Test the function
arr = [3, 6, 8, 10, 1, 2, 1]
sorted_arr = quicksort(arr)
print(sorted_arr)
