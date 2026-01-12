def show_menu():
    print("------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Amount Spent")
    print("4. Categorize summary")
    print("5. Searching")
    print("6. Summarytotxtfile")
    print("7. Exit")

import csv
from datetime import datetime

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    date = datetime.now().strftime("%Y-%m-%d")

    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("Expense added successfully!\n")


def total_expenses():
    with open("expenses.csv","r") as file:
        total=0
        for parts in file:
            calc=parts.strip().split(",")
            amount=calc[1]
            total+= int(amount)
        print(f"Total expenses {total}")

def show_expenses():
    try:
        with open("expenses.csv", "r") as file:
            print("--------------------------------------------")
            print(f"{'DATE':<15} | {'AMOUNT':<10} | CATEGORY")
            print("--------------------------------------------")

            rows = [row.strip().split(",") for row in file]
            for date, amount, category in rows:
                print(f"{date:<15} | {amount:<10} | {category}")

            print("--------------------------------------------")
    except FileNotFoundError:
        print("No expenses found. Add some first!\n")


def category_summary():
    d={}
    with open("expenses.csv","r") as file:
        for row in file:
           calc=row.strip().split(",")
           amount=calc[1]
           d[calc[2]]=d.get(calc[2],0)+int(amount)
        print("\n------ Category Summary ------")
        for category, total in d.items():
           print(f"{category}: {total}")
        print("------------------------------\n")

def search_expenses():
    query = input("Enter date or category to search: ").lower()
    found = False
    print("--------------------------------------------")
    print(f"{'DATE':<15} | {'AMOUNT':<10} | CATEGORY")
    print("--------------------------------------------")
    with open("expenses.csv", "r") as file:
        for row in file:
            parts = row.strip().split(",")
            date, amount, category = parts[0], parts[1], parts[2]
            if query in date.lower() or query in category.lower():
                print(f"{date:<15} | {amount:<10} | {category}")
                found = True
    if not found:
        print("No matching expenses found.")
    print("--------------------------------------------")

def summarytofile():
    d = {}

    try:
        with open("expenses.csv", "r") as file:
            for row in file:
                parts = row.strip().split(",")
                amount = int(parts[1])
                category = parts[2]
                d[category] = d.get(category, 0) + amount

        with open("summary.txt", "w") as out:
            out.write("------ Category Summary ------\n")
            for category, amount in d.items():
                out.write(f"{category}: {amount}\n")
            out.write("------------------------------\n")

        print("Summary exported to summary.txt")

    except FileNotFoundError:
        print("Error: expenses.csv not found.")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Adding new expense...")
        add_expense()
    elif choice == "2":
        print("Viewing all expenses...")
        show_expenses()
    elif choice == "3":
        print("Calculating total...")
        total_expenses()
    elif choice == "4":
        category_summary()
    elif choice == "5":
        search_expenses()
    elif choice == "6":
        summarytofile()
    elif choice == "7":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")