# ====================================================
#   🔐 Password Generator — Soham Dey (Soham5454)
# ====================================================

import random
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    chars = string.ascii_lowercase
    guaranteed = []
    if use_upper:
        chars += string.ascii_uppercase
        guaranteed.append(random.choice(string.ascii_uppercase))
    if use_digits:
        chars += string.digits
        guaranteed.append(random.choice(string.digits))
    if use_symbols:
        symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        chars += symbols
        guaranteed.append(random.choice(symbols))
    remaining = length - len(guaranteed)
    password = guaranteed + [random.choice(chars) for _ in range(remaining)]
    random.shuffle(password)
    return ''.join(password)

def strength(password):
    score = 0
    if len(password) >= 12: score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password): score += 1
    return ["⚠️  Weak", "🟡 Fair", "🟠 Good", "🟢 Strong", "🔥 Very Strong"][score]

def main():
    print("=" * 45)
    print("       🔐  Password Generator")
    print("=" * 45)
    while True:
        try:
            length = int(input("\n  Password length (8-64): "))
            if not 8 <= length <= 64:
                print("  ❌ Length must be between 8 and 64!")
                continue
        except ValueError:
            print("  ❌ Enter a valid number!")
            continue

        upper   = input("  Include UPPERCASE? (y/n): ").lower() == 'y'
        digits  = input("  Include numbers?   (y/n): ").lower() == 'y'
        symbols = input("  Include symbols?   (y/n): ").lower() == 'y'

        print("\n  Generated Passwords:")
        print("  " + "-" * 40)
        for i in range(5):
            pwd = generate_password(length, upper, digits, symbols)
            print(f"  {i+1}. {pwd}")
        print("  " + "-" * 40)
        print(f"  Strength: {strength(generate_password(length, upper, digits, symbols))}")

        again = input("\n  Generate more? (y/n): ").lower()
        if again != 'y':
            print("\n  Stay secure! 🔒\n")
            break

if __name__ == "__main__":
    main()
