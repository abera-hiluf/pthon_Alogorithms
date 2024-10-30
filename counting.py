def count_even_numbers(arr):
    even_numbers = [] # Initialize the counter
    for i in arr:  # Iterate over each element
        if i % 2 == 0:  # Check if the number is even
            even_numbers.append(i)  # Increment the counter
    return even_numbers  # Return the total count of even numbers

arr = [4, 5, 2, 8, 18, 10]
result = count_even_numbers(arr)
print(result)