# ==========================================================
#   🪨 Rock Paper Scissors — Soham Dey (Soham5454)
# ==========================================================

import random
import time

CHOICES  = ['rock', 'paper', 'scissors']
EMOJI    = {'rock':'🪨', 'paper':'📄', 'scissors':'✂️'}
BEATS    = {'rock':'scissors', 'paper':'rock', 'scissors':'paper'}

def get_result(player, computer):
    if player == computer:              return "draw"
    if BEATS[player] == computer:       return "win"
    return "lose"

def ascii_art(choice):
    art = {
        'rock':     ["    _____  ","   /     \\ ","  | () () |","   \\  ^  / ","    |||||  "],
        'paper':    ["  _______  "," |       | "," |       | "," |       | "," |_______| "],
        'scissors': ["  __  __  "," / \\/ \\ ","| ><><>< |"," \\ /\\ / ","  ~~  ~~  "],
    }
    return art[choice]

def show_vs(p, c):
    pa, ca = ascii_art(p), ascii_art(c)
    print()
    for pl, cl in zip(pa, ca):
        print(f"    {pl}        {cl}")
    print(f"\n    {EMOJI[p]} YOU       {EMOJI[c]} CPU\n")

def main():
    print("=" * 45)
    print("     🪨📄✂️   Rock Paper Scissors")
    print("=" * 45)

    wins = losses = draws = 0
    streak = 0

    while True:
        total = wins + losses + draws
        if total > 0:
            print(f"\n  Score → ✅ {wins}W  ❌ {losses}L  🤝 {draws}D", end="")
            if streak > 1: print(f"  🔥 {streak} streak!", end="")
            print()

        print("\n  1. Rock  2. Paper  3. Scissors  0. Quit")
        choice = input("  Your move: ").strip()

        if choice == '0':
            print(f"\n  Final: {wins}W / {losses}L / {draws}D")
            if wins > losses: print("  🏆 You won overall! Amazing!")
            elif losses > wins: print("  😅 CPU wins this time. Rematch?")
            else: print("  🤝 It's a tie overall!")
            print("  GG! 👋\n")
            break

        moves = {'1':'rock', '2':'paper', '3':'scissors'}
        if choice not in moves:
            print("  ❌ Invalid choice!")
            continue

        player   = moves[choice]
        print("\n  3... 2... 1... SHOOT!")
        time.sleep(0.8)
        computer = random.choice(CHOICES)
        result   = get_result(player, computer)

        show_vs(player, computer)

        if result == "win":
            print(f"  🎉 YOU WIN! {EMOJI[player]} beats {EMOJI[computer]}!")
            wins   += 1; streak += 1
        elif result == "lose":
            print(f"  😢 YOU LOSE! {EMOJI[computer]} beats {EMOJI[player]}!")
            losses += 1; streak  = 0
        else:
            print(f"  🤝 DRAW! Both chose {EMOJI[player]}!")
            draws  += 1; streak  = 0

if __name__ == "__main__":
    main()
