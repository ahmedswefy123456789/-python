import random

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 3.14).")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer (e.g., 5).")

def menu():
    print("\nChoose a scenario:")
    print("1: List order")
    print("2: Generate sequence")
    print("3: Running total and average")
    print("4: Unique sorted numbers")
    print("5: People with favorite color")
    print("6: Word count in sentence")
    print("7: Student scores")
    print("8: Shopping cart")
    print("9: Number guessing game")
    print("0: Quit")

def scenario_1():
    numbers = []
    for i in range(5):
        num = input_float(f"Enter number {i+1}: ")
        numbers.append(num)
    print("Ascending:", sorted(numbers))
    print("Descending:", sorted(numbers, reverse=True))

def scenario_2():
    length = input_int("Enter sequence length: ")
    start = input_int("Enter start number: ")
    seq = [start + i for i in range(length)]
    print("Sequence:", seq)

def scenario_3():
    total = 0
    count = 0
    while True:
        entry = input("Enter a number (or 'done'): ")
        if entry.lower() == "done":
            break
        try:
            num = float(entry)
            total += num
            count += 1
        except ValueError:
            print("Invalid input! Please enter a valid number (e.g., 2.5) or 'done'.")
    if count > 0:
        print("Total:", total)
        print("Count:", count)
        print("Average:", total / count)
    else:
        print("No valid numbers entered.")

def scenario_4():
    while True:
        nums = input("Enter numbers separated by spaces: ")
        try:
            nums_list = list(map(float, nums.split()))
            unique_sorted = sorted(set(nums_list))
            print("Result:", unique_sorted)
            break
        except ValueError:
            print("Invalid input! Please enter numbers separated by spaces (e.g., 1 2 3.5).")

def scenario_5():
    people = {}
    while True:
        name = input("Enter person's name (or 'done'): ")
        if name.lower() == "done":
            break
        color = input("Enter favorite color: ")
        people[name] = color
    print("People and their favorite colors:")
    for name, color in people.items():
        print(f"{name}: {color}")

def scenario_6():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    print("Word counts:")
    for word, count in word_count.items():
        print(f"{word}: {count}")

def scenario_7():
    students = []
    scores = []
    for i in range(5):
        name = input(f"Enter student {i+1} name: ")
        score = input_float(f"Enter {name}'s score: ")
        students.append(name)
        scores.append(score)
    print("Highest score:", max(scores))
    print("Lowest score:", min(scores))
    print("Average score:", sum(scores)/len(scores))

def scenario_8():
    cart = {}
    while True:
        action = input("Add, Remove, View, or Quit: ").lower()
        if action == "add":
            name = input("Item name: ")
            price = input_float("Item price: ")
            cart[name] = price
        elif action == "remove":
            name = input("Item name to remove: ")
            if name in cart:
                cart.pop(name)
            else:
                print("Item not found in cart.")
        elif action == "view":
            for name, price in cart.items():
                print(f"{name}: ${price:.2f}")
        elif action == "quit":
            break
        else:
            print("Invalid action! Valid actions: Add, Remove, View, Quit.")
    total = sum(cart.values())
    print("Total cost: $%.2f" % total)

def scenario_9():
    number = random.randint(1, 20)
    attempts = 0
    while True:
        guess = input("Guess the number (1-20): ")
        try:
            guess = int(guess)
            if not 1 <= guess <= 20:
                print("Invalid input! Please enter an integer between 1 and 20.")
                continue
            attempts += 1
            if guess < number:
                print("Too low.")
            elif guess > number:
                print("Too high.")
            else:
                print(f"Correct! Attempts: {attempts}")
                break
        except ValueError:
            print("Invalid input! Please enter an integer between 1 and 20.")

def main():
    while True:
        menu()
        choice = input("Enter scenario number: ")
        if choice == "1":
            scenario_1()
        elif choice == "2":
            scenario_2()
        elif choice == "3":
            scenario_3()
        elif choice == "4":
            scenario_4()
        elif choice == "5":
            scenario_5()
        elif choice == "6":
            scenario_6()
        elif choice == "7":
            scenario_7()
        elif choice == "8":
            scenario_8()
        elif choice == "9":
            scenario_9()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number from 0 to 9.")

if __name__ == "__main__":
    main()