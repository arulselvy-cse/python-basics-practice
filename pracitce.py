numbers = []
for i in range(5):
num = int(input(f"Enter a number {i+1}"))
numbers.append(num)
min_value = min(numbers)
max_value = max(numbers)
print("Numbers entered:",numbers)
print("Maximum_value:",max_value)
print("Minimum_value:",min_value)
