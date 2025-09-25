import csv
from datetime import datetime

def log_expense(amount, category):
    with open("expenses.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), category, amount])
    print("Expense logged!")

def show_summary():
    total = 0
    with open("expenses.csv", mode="r") as file:
        reader = csv.reader(file)
        print("\nDate\t\t\tCategory\tAmount")
        print("-" * 40)
        for row in reader:
            print(f"{row[0]}\t{row[1]}\t₹{row[2]}")
            total += float(row[2])
    print(f"\nTotal Expenses: ₹{total:.2f}")

# Example usage
log_expense(250, "Groceries")
log_expense(120, "Transport")
show_summary()
