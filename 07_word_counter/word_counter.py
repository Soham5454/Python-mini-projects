# ====================================================
#   📝 Word Counter — Soham Dey (Soham5454)
# ====================================================

import os
import string
from collections import Counter

def analyze(text):
    words      = text.split()
    chars_all  = len(text)
    chars_nsp  = len(text.replace(" ","").replace("\n",""))
    word_count = len(words)
    sentences  = text.count('.')+text.count('!')+text.count('?')
    paragraphs = len([p for p in text.split('\n\n') if p.strip()])
    lines      = text.count('\n') + 1
    avg_word   = sum(len(w.strip(string.punctuation)) for w in words) / max(word_count, 1)

    # top 10 words (ignore common ones)
    stop = {"the","a","an","is","it","in","on","at","to","of","and","or",
            "but","for","with","was","are","be","this","that","i","you","we"}
    clean_words = [w.strip(string.punctuation).lower() for w in words
                   if w.strip(string.punctuation).lower() not in stop and len(w) > 1]
    top_words = Counter(clean_words).most_common(10)

    print("\n  " + "="*45)
    print("       📊 Text Analysis Results")
    print("  " + "="*45)
    print(f"  📝 Words        : {word_count}")
    print(f"  🔤 Characters   : {chars_all} (without spaces: {chars_nsp})")
    print(f"  📖 Sentences    : {sentences}")
    print(f"  📄 Paragraphs   : {paragraphs}")
    print(f"  📏 Lines        : {lines}")
    print(f"  📐 Avg Word Len : {avg_word:.1f} characters")
    print(f"  ⏱️  Read Time    : ~{max(1, word_count // 200)} min")

    if top_words:
        print("\n  🔝 Top 10 Most Used Words:")
        print("  " + "-"*30)
        for word, count in top_words:
            bar = "▓" * count
            print(f"  {word:<18} {count:>3}x  {bar}")
    print("  " + "="*45)

def main():
    print("=" * 45)
    print("         📝  Word Counter & Analyzer")
    print("=" * 45)
    while True:
        print("\n  1. Type / Paste text")
        print("  2. Analyze a .txt file")
        print("  0. Exit")
        choice = input("\n  Choice: ").strip()

        if choice == '1':
            print("\n  Paste your text below.")
            print("  Type 'END' on a new line when done:\n")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == 'END': break
                lines.append(line)
            text = '\n'.join(lines)
            if text.strip(): analyze(text)
            else: print("  ❌ No text entered!")

        elif choice == '2':
            path = input("  Enter file path: ").strip().strip('"')
            if os.path.exists(path):
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    text = f.read()
                analyze(text)
            else:
                print("  ❌ File not found!")

        elif choice == '0':
            print("\n  Happy writing! ✍️\n")
            break
        else:
            print("  ❌ Invalid choice!")

if __name__ == "__main__":
    main()
