def show_menu():
    print("------ Expense Tracker ------")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Amount Spent")
    print("4. Exit")
    print("5. Categorize summary")

import csv
from datetime import datetime

def add_expense():
    amount = input("Enter amount: ")
    category = input("Enter category: ")

    date = datetime.now().strftime("%Y-%m-%d")

    # Open CSV file in append mode
    with open("expenses.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category])

    print("Expense added successfully!\n")

def view_expenses():
    try:
        with open("expenses.csv", "r") as file:
            reader = csv.reader(file)
            print("\n------ All Expenses ------")
            for row in reader:
                print(f"Date: {row[0]} | Amount: {row[1]} | Category: {row[2]}")
            print()
    except FileNotFoundError:
        print("No expenses found. Add some first!\n")

def total_expenses():
    with open("expenses.csv","r") as file:
        total=0
        for parts in file:
            calc=parts.strip().split(",")
            amount=calc[1]
            total+= int(amount)
        print(f"Total expenses {total}")

def show_expenses():
    print("--------------------------------------------")
    print(f"{'DATE':<15} | {'AMOUNT':<10} | CATEGORY")
    print("--------------------------------------------")
    
    with open("expenses.csv", "r") as file:
            rows=[row.strip().split(",") for row in file]
            for date,amount,category in rows:
               print(f"{date:<15} | {amount:<10} | {category}")

            print("--------------------------------------------")

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
        print("Exiting program...")
        break
    elif choice == "5":
        category_summary()
    else:
        print("Invalid choice. Try again.")
