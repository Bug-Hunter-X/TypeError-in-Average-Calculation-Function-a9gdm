def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

# Example usage
data = [10, 20, 'a', 30, 40.5]
average = calculate_average(data)
print(f"The average is: {average}")

#Alternative solution using exception handling
def calculate_average_with_exception_handling(numbers):
    try:
        return sum(numbers) / len(numbers)
    except TypeError:
        print("Error: List contains non-numeric values.")
        return 0

data = [10, 20, 'a', 30, 40.5]
average = calculate_average_with_exception_handling(data)
print(f"The average is: {average}") 