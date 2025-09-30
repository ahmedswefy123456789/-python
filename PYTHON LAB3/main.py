import sys
from tasks import task1_math_automation, task2_regex_log_cleaner, task3_datetime_reminder, task4_product_data_transformer, task5_os_file_manager, task6_random_data_generator

def print_menu():
    print("""
Select a task to run:
1) Math Automation
2) Regex Log Cleaner
3) Datetime Reminder Script
4) Product Data Transformer
5) OS File Manager
6) Random Data Generator
0) Exit
""")

def get_choice():
    while True:
        choice = input("Enter task number: ")
        if choice.isdigit() and 0 <= int(choice) <= 6:
            return int(choice)
        print("Invalid choice. Please enter a number between 0 and 6.")

def main():
    while True:
        print_menu()
        choice = get_choice()
        if choice == 0:
            print("Goodbye!")
            sys.exit()
        elif choice == 1:
            task1_math_automation.math_automation()
        elif choice == 2:
            task2_regex_log_cleaner.regex_log_cleaner()
        elif choice == 3:
            task3_datetime_reminder.datetime_reminder()
        elif choice == 4:
            task4_product_data_transformer.product_data_transformer()
        elif choice == 5:
            task5_os_file_manager.os_file_manager()
        elif choice == 6:
            task6_random_data_generator.random_data_generator()

if __name__ == "__main__":
    main()
