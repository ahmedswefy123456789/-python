import math
from tasks.decorators import log_time

def get_numbers():
    while True:
        user_input = input("Enter numbers (comma-separated): ")
        try:
            numbers = [float(x.strip()) for x in user_input.split(',')]
            return numbers
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by commas.")

@log_time
def math_automation():
    numbers = get_numbers()
    results = []
    for num in numbers:
        result = {
            'number': num,
            'floor': math.floor(num),
            'ceil': math.ceil(num),
            'sqrt': math.sqrt(num) if num >= 0 else 'NaN',
            'circle_area': math.pi * num * num if num >= 0 else 'NaN'
        }
        results.append(result)
    with open('math_report.txt', 'w') as f:
        for r in results:
            f.write(f"Number: {r['number']}, Floor: {r['floor']}, Ceil: {r['ceil']}, Sqrt: {r['sqrt']}, Area: {r['circle_area']}\n")
    print("math_report.txt created. Contents:")
    with open('math_report.txt', 'r') as f:
        print(f.read())
