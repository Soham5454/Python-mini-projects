# ======================================================
#   💰 Expense Tracker — Soham Dey (Soham5454)
# ======================================================

import json
import os
from datetime import datetime

FILE = "expenses.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return []

def save(data):
    with open(FILE, 'w') as f:
        json.dump(data, f, indent=2)

def add_expense(data):
    print("\n  📝 Add New Expense")
    categories = ["Food","Transport","Shopping","Entertainment","Health","Education","Other"]
    for i, c in enumerate(categories, 1):
        print(f"  {i}. {c}")
    try:
        cat_i = int(input("  Category (1-7): ")) - 1
        category = categories[cat_i] if 0 <= cat_i < len(categories) else "Other"
        amount = float(input("  Amount (Rs): "))
        desc   = input("  Description : ").strip() or "No description"
    except ValueError:
        print("  ❌ Invalid input!")
        return
    entry = {"date": datetime.now().strftime("%d-%m-%Y %H:%M"),
             "category": category, "amount": amount, "desc": desc}
    data.append(entry)
    save(data)
    print(f"  ✅ Added: Rs {amount:.2f} for {category}")

def view_all(data):
    if not data:
        print("\n  📭 No expenses recorded yet!")
        return
    print("\n  📋 All Expenses:")
    print("  " + "-"*60)
    total = 0
    for i, e in enumerate(data, 1):
        print(f"  {i:2}. [{e['date']}] {e['category']:<14} Rs {e['amount']:>8.2f}  — {e['desc']}")
        total += e['amount']
    print("  " + "-"*60)
    print(f"  💵 TOTAL: Rs {total:.2f}")

def summary(data):
    if not data:
        print("\n  📭 No expenses yet!")
        return
    cats = {}
    for e in data:
        cats[e['category']] = cats.get(e['category'], 0) + e['amount']
    total = sum(cats.values())
    print("\n  📊 Expense Summary by Category:")
    print("  " + "-"*40)
    for cat, amt in sorted(cats.items(), key=lambda x: -x[1]):
        bar = "█" * int((amt / total) * 20)
        print(f"  {cat:<14} Rs {amt:>8.2f}  {bar}")
    print("  " + "-"*40)
    print(f"  💵 TOTAL: Rs {total:.2f}")

def delete_expense(data):
    view_all(data)
    if not data: return
    try:
        i = int(input("\n  Enter entry number to delete: ")) - 1
        if 0 <= i < len(data):
            removed = data.pop(i)
            save(data)
            print(f"  ✅ Deleted: Rs {removed['amount']} — {removed['desc']}")
        else:
            print("  ❌ Invalid number!")
    except ValueError:
        print("  ❌ Invalid input!")

def main():
    print("=" * 45)
    print("       💰  Expense Tracker")
    print("=" * 45)
    data = load()
    while True:
        print("\n  1. Add Expense")
        print("  2. View All Expenses")
        print("  3. Summary by Category")
        print("  4. Delete an Expense")
        print("  0. Exit")
        choice = input("\n  Choice: ").strip()
        if   choice == '1': add_expense(data)
        elif choice == '2': view_all(data)
        elif choice == '3': summary(data)
        elif choice == '4': delete_expense(data)
        elif choice == '0':
            print("\n  Keep saving money! 💸\n")
            break
        else:
            print("  ❌ Invalid choice!")

if __name__ == "__main__":
    main()
