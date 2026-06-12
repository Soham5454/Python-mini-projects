# ====================================================
#   🎲 Dice Roller — Soham Dey (Soham5454)
# ====================================================

import random
import time

DICE_ART = {
    1: ["┌─────────┐","│         │","│    ●    │","│         │","└─────────┘"],
    2: ["┌─────────┐","│  ●      │","│         │","│      ●  │","└─────────┘"],
    3: ["┌─────────┐","│  ●      │","│    ●    │","│      ●  │","└─────────┘"],
    4: ["┌─────────┐","│  ●   ●  │","│         │","│  ●   ●  │","└─────────┘"],
    5: ["┌─────────┐","│  ●   ●  │","│    ●    │","│  ●   ●  │","└─────────┘"],
    6: ["┌─────────┐","│  ●   ●  │","│  ●   ●  │","│  ●   ●  │","└─────────┘"],
}

def roll_dice(num_dice=1, sides=6):
    return [random.randint(1, sides) for _ in range(num_dice)]

def show_dice(values):
    if len(values) > 6:
        print(f"  Results: {values}")
        return
    rows = [[] for _ in range(5)]
    for v in values:
        if v in DICE_ART:
            for i, row in enumerate(DICE_ART[v]):
                rows[i].append(row)
    for row in rows:
        print("  " + "  ".join(row))

def stats(history):
    if not history: return
    flat = [v for roll in history for v in roll]
    print(f"\n  📊 Session Stats:")
    print(f"  Total rolls : {len(history)}")
    print(f"  Total dice  : {len(flat)}")
    print(f"  Highest     : {max(flat)}")
    print(f"  Lowest      : {min(flat)}")
    print(f"  Average     : {sum(flat)/len(flat):.1f}")
    freq = {i: flat.count(i) for i in range(1, 7) if flat.count(i) > 0}
    print(f"  Frequency   : {freq}")

def main():
    print("=" * 40)
    print("         🎲  Dice Roller")
    print("=" * 40)
    history = []

    while True:
        print("\n  1. Roll standard dice (D6)")
        print("  2. Roll custom dice (D4/D8/D10/D12/D20)")
        print("  3. Roll multiple dice")
        print("  4. View session stats")
        print("  0. Exit")
        choice = input("\n  Choice: ").strip()

        if choice == '1':
            input("  Press ENTER to roll... 🎲")
            values = roll_dice(1, 6)
            print(f"\n  🎲 Rolling", end="", flush=True)
            for _ in range(3): print(".", end="", flush=True); time.sleep(0.3)
            print()
            show_dice(values)
            print(f"\n  Result: {values[0]}")
            history.append(values)

        elif choice == '2':
            print("  Dice types: 4, 6, 8, 10, 12, 20")
            try:
                sides = int(input("  Sides (e.g. 20 for D20): "))
                if sides < 2: raise ValueError
            except ValueError:
                print("  ❌ Invalid dice type!"); continue
            input(f"  Press ENTER to roll D{sides}... 🎲")
            values = roll_dice(1, sides)
            print(f"\n  🎲 D{sides} Result: {values[0]}")
            history.append(values)

        elif choice == '3':
            try:
                n = int(input("  How many dice? (1-10): "))
                if not 1 <= n <= 10: raise ValueError
            except ValueError:
                print("  ❌ Enter a number between 1 and 10!"); continue
            input(f"  Press ENTER to roll {n} dice... 🎲")
            values = roll_dice(n, 6)
            print(f"\n  🎲 Rolling {n} dice", end="", flush=True)
            for _ in range(3): print(".", end="", flush=True); time.sleep(0.3)
            print()
            show_dice(values)
            print(f"\n  Results : {values}")
            print(f"  Total   : {sum(values)}")
            print(f"  Average : {sum(values)/len(values):.1f}")
            history.append(values)

        elif choice == '4':
            stats(history)

        elif choice == '0':
            stats(history)
            print("\n  May the dice be ever in your favour! 🎲\n")
            break
        else:
            print("  ❌ Invalid choice!")

if __name__ == "__main__":
    main()
