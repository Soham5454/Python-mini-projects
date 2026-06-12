# ========================================================
#   💱 Currency Converter — Soham Dey (Soham5454)
# ========================================================

# Note: Rates are approximate — for live rates use an API

RATES_TO_USD = {
    "USD": 1.0,
    "INR": 0.012,
    "EUR": 1.08,
    "GBP": 1.27,
    "JPY": 0.0067,
    "CAD": 0.74,
    "AUD": 0.65,
    "CNY": 0.14,
    "SGD": 0.74,
    "AED": 0.27,
    "BTC": 67000.0,
}

FLAGS = {
    "USD":"🇺🇸","INR":"🇮🇳","EUR":"🇪🇺","GBP":"🇬🇧","JPY":"🇯🇵",
    "CAD":"🇨🇦","AUD":"🇦🇺","CNY":"🇨🇳","SGD":"🇸🇬","AED":"🇦🇪","BTC":"₿ ",
}

NAMES = {
    "USD":"US Dollar","INR":"Indian Rupee","EUR":"Euro","GBP":"British Pound",
    "JPY":"Japanese Yen","CAD":"Canadian Dollar","AUD":"Australian Dollar",
    "CNY":"Chinese Yuan","SGD":"Singapore Dollar","AED":"UAE Dirham","BTC":"Bitcoin",
}

def convert(amount, from_cur, to_cur):
    usd    = amount * RATES_TO_USD[from_cur]
    result = usd / RATES_TO_USD[to_cur]
    return result

def show_currencies():
    print("\n  Available Currencies:")
    print("  " + "-"*40)
    currencies = list(RATES_TO_USD.keys())
    for i in range(0, len(currencies), 3):
        row = currencies[i:i+3]
        for c in row:
            print(f"  {FLAGS[c]} {c:<4} {NAMES[c]:<20}", end="")
        print()

def main():
    print("=" * 48)
    print("        💱  Currency Converter")
    print("  (Offline mode — approximate rates)")
    print("=" * 48)

    while True:
        print("\n  1. Convert currency")
        print("  2. Show all currencies")
        print("  3. Show all rates vs INR")
        print("  0. Exit")
        choice = input("\n  Choice: ").strip()

        if choice == '1':
            show_currencies()
            from_cur = input("\n  From currency (e.g. INR): ").upper().strip()
            to_cur   = input("  To currency   (e.g. USD): ").upper().strip()
            if from_cur not in RATES_TO_USD or to_cur not in RATES_TO_USD:
                print("  ❌ Invalid currency code!")
                continue
            try:
                amount = float(input(f"  Amount in {from_cur}: "))
            except ValueError:
                print("  ❌ Invalid amount!")
                continue
            result = convert(amount, from_cur, to_cur)
            print(f"\n  {FLAGS[from_cur]} {amount:,.2f} {from_cur} = {FLAGS[to_cur]} {result:,.4f} {to_cur}")
            print(f"  ({NAMES[from_cur]} → {NAMES[to_cur]})")
            # show multi-currency breakdown
            print("\n  📊 Quick conversion table:")
            for cur in ["USD","INR","EUR","GBP","JPY"]:
                if cur != from_cur:
                    r = convert(amount, from_cur, cur)
                    print(f"    {FLAGS[cur]} {cur}: {r:>12,.4f}")

        elif choice == '2':
            show_currencies()

        elif choice == '3':
            print("\n  📊 1 unit of each currency in INR:")
            print("  " + "-"*35)
            for cur, rate in RATES_TO_USD.items():
                inr = convert(1, cur, "INR")
                print(f"  {FLAGS[cur]} 1 {cur:<4} = ₹ {inr:>10,.2f}")

        elif choice == '0':
            print("\n  Happy trading! 💸\n")
            break
        else:
            print("  ❌ Invalid choice!")

if __name__ == "__main__":
    main()
