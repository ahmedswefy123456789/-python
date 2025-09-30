from datetime import datetime

def get_date():
    while True:
        date_str = input("Enter a date (YYYY-MM-DD): ")
        try:
            date = datetime.strptime(date_str, "%Y-%m-%d")
            return date_str, date
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def datetime_reminder():
    date_str, date = get_date()
    today = datetime.now()
    delta = (date - today).days
    if delta < 0:
        print("This date has already passed.")
    else:
        with open('reminders.txt', 'a') as f:
            f.write(f"{date_str} -> {delta} days left\n")
        print(f"Reminder saved: {date_str} -> {delta} days left")
