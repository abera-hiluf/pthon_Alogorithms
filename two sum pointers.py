def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (arr[left], arr[right])  # Return the pair of numbers
        
        elif current_sum < target:
            left += 1  # Increase the sum by moving the left pointer to the right
        else:
            right -= 1  # Decrease the sum by moving the right pointer to the left
    
    return None  # If no pair is found

# Example usage:
arr = [1, 3, 4, 5, 7, 10, 11]
target = 9
result = two_sum_sorted(arr, target)
print(result)