def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)

data = [10, 20, 30, 'a']
average = calculate_average(data)
print(f"Average: {average}")

data2 = [10,20,30,40,50]
average2 = calculate_average(data2)
print(f"Average: {average2}") 