numbers = [5, 2, 8, 1, 9, 3, 7, 4, 6, 10]

print(f"Original List: {numbers}")
print("---")

# 1. Find the Sum using sum()
total_sum = sum(numbers)
print(f"1. Sum (using sum()): {total_sum}")

# 2. Find the Average
list_length = len(numbers)
average = total_sum / list_length
print(f"2. Average: {average}")

# 3. Find the Maximum using max()
max_value = max(numbers)
print(f"3. Maximum (using max()): {max_value}")

# 4. Find the Minimum using min()
min_value = min(numbers)
print(f"4. Minimum (using min()): {min_value}")

# 5. Reverse the list using slicing [::-1]
# This creates a new, reversed copy of the list.
reversed_list = numbers[::-1]
print(f"5. Reversed List (using [::-1]): {reversed_list}")