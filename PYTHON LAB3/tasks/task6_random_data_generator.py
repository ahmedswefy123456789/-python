import random
import csv

def get_count():
    while True:
        val = input("How many random numbers to generate? ")
        if val.isdigit() and int(val) > 0:
            return int(val)
        print("Please enter a positive integer.")

def random_data_generator():
    count = get_count()
    numbers = [random.randint(1, 100) for _ in range(count)]
    with open('random_numbers.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['index', 'value'])
        for i, num in enumerate(numbers, 1):
            writer.writerow([i, num])
    avg = sum(numbers) / count
    print(f"Generated {count} numbers. Average: {avg:.2f}")
