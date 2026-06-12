# ============================================
#   🧮 Calculator — Soham Dey (Soham5454)
# ============================================

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
def modulus(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a % b
def power(a, b):    return a ** b

operations = {
    '1': ('+',  add),
    '2': ('-',  subtract),
    '3': ('*',  multiply),
    '4': ('/',  divide),
    '5': ('%',  modulus),
    '6': ('**', power),
}

def main():
    print("=" * 40)
    print("        🧮  Python Calculator")
    print("=" * 40)
    while True:
        print("\n  1. Addition       2. Subtraction")
        print("  3. Multiply       4. Division")
        print("  5. Modulus        6. Power")
        print("  0. Exit")
        choice = input("\n  Choose operation: ").strip()
        if choice == '0':
            print("\n  Goodbye! 👋\n")
            break
        if choice not in operations:
            print("  ❌ Invalid choice!")
            continue
        try:
            a = float(input("  Enter first number : "))
            b = float(input("  Enter second number: "))
        except ValueError:
            print("  ❌ Please enter valid numbers!")
            continue
        symbol, func = operations[choice]
        result = func(a, b)
        if isinstance(result, float) and result == int(result):
            result = int(result)
        print(f"\n  ✅  {a} {symbol} {b} = {result}")

if __name__ == "__main__":
    main()
