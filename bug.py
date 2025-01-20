def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case
    return sum(numbers) / len(numbers)

# Example usage that can lead to an error
data = [10, 20, 'a', 30]
average = calculate_average(data)
print(f"The average is: {average}")