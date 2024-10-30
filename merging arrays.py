def merge_sorted_arrays(arr1, arr2):
    # Create a new array to hold the merged result
    merged_array = []
    i, j = 0, 0

    # Iterate through both arrays until one is exhausted
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    # Append remaining elements of arr1 (if any)
    while i < len(arr1):
        merged_array.append(arr1[i])
        i += 1

    # Append remaining elements of arr2 (if any)
    while j < len(arr2):
        merged_array.append(arr2[j])
        j += 1

    return merged_array

# Example Usage
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
merged = merge_sorted_arrays(arr1, arr2)
print(merged)  # Output: [1, 2, 3, 4, 5, 6]

def mergeLists(list1, list2):
    merged = []
    first, second = 0, 0

    while first < len(list1) and second < len(list2):
        if list1[first] < list2[second]:
            merged.append(list1[first])
            first += 1
        else:
            merged.append(list2[second])
            second += 1

    # Extend merged with the remaining elements of list1 and list2
    merged.extend(list1[first:])
    merged.extend(list2[second:])

    return merged

# Example usage
list1 = [1, 2, 4]
list2 = [1, 3, 4]
result = mergeLists(list1, list2)
print(result)  # Output the merged list
