# ======================================================
#   🎯 Number Guessing Game — Soham Dey (Soham5454)
# ======================================================

import random
import time

def play(difficulty):
    settings = {
        '1': ("Easy",   1,   50,  10),
        '2': ("Medium", 1,  100,   7),
        '3': ("Hard",   1,  200,   5),
        '4': ("Expert", 1, 1000,   7),
    }
    name, low, high, attempts = settings[difficulty]
    secret  = random.randint(low, high)
    guesses = 0
    history = []

    print(f"\n  🎯 [{name}] Guess a number between {low} and {high}")
    print(f"  You have {attempts} attempts!\n")

    while guesses < attempts:
        remaining = attempts - guesses
        try:
            guess = int(input(f"  Attempt {guesses+1}/{attempts} → "))
        except ValueError:
            print("  ❌ Enter a valid number!")
            continue

        guesses  += 1
        history.append(guess)
        diff      = abs(secret - guess)

        if guess == secret:
            print(f"\n  🎉 CORRECT! The number was {secret}!")
            print(f"  ✅ Solved in {guesses} attempt(s)!")
            stars = "⭐" * max(1, attempts - guesses + 1)
            print(f"  Rating: {stars}")
            return True
        elif guess < secret:
            hint = "🔥 Very warm!" if diff <= 5 else ("☀️ Warm!" if diff <= 15 else "❄️ Too low!")
            print(f"  ↑  Go HIGHER  —  {hint}  ({remaining-1} left)")
        else:
            hint = "🔥 Very warm!" if diff <= 5 else ("☀️ Warm!" if diff <= 15 else "❄️ Too high!")
            print(f"  ↓  Go LOWER   —  {hint}  ({remaining-1} left)")

    print(f"\n  💀 Game Over! The number was {secret}")
    print(f"  Your guesses: {history}")
    return False

def main():
    print("=" * 45)
    print("       🎯  Number Guessing Game")
    print("=" * 45)
    wins = losses = 0

    while True:
        print("\n  Select Difficulty:")
        print("  1. Easy   (1–50,   10 attempts)")
        print("  2. Medium (1–100,   7 attempts)")
        print("  3. Hard   (1–200,   5 attempts)")
        print("  4. Expert (1–1000,  7 attempts)")
        print("  0. Quit")
        d = input("\n  Choice: ").strip()
        if d == '0':
            print(f"\n  Final Score → Wins: {wins}  Losses: {losses}")
            print("  Thanks for playing! 👋\n")
            break
        if d not in ('1','2','3','4'):
            print("  ❌ Invalid choice!")
            continue
        if play(d): wins   += 1
        else:       losses += 1
        print(f"\n  Score → ✅ Wins: {wins}  ❌ Losses: {losses}")

if __name__ == "__main__":
    main()
