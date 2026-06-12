# ================================================
#   🧠 Quiz Game — Soham Dey (Soham5454)
# ================================================

import random
import time

questions = [
    {"q": "What does CPU stand for?",
     "options": ["A. Central Process Unit", "B. Central Processing Unit",
                 "C. Computer Personal Unit", "D. Core Processing Unit"],
     "answer": "B", "fact": "The CPU is the brain of the computer!"},

    {"q": "Which language is known as the 'mother of all languages'?",
     "options": ["A. Python", "B. Java", "C. C", "D. Assembly"],
     "answer": "C", "fact": "C was created by Dennis Ritchie in 1972."},

    {"q": "What does RAM stand for?",
     "options": ["A. Random Access Memory", "B. Read Access Memory",
                 "C. Run Application Memory", "D. Random Active Module"],
     "answer": "A", "fact": "RAM is temporary memory used while programs run."},

    {"q": "Which company created Python?",
     "options": ["A. Google", "B. Microsoft", "C. Guido van Rossum", "D. Apple"],
     "answer": "C", "fact": "Guido van Rossum created Python in 1991."},

    {"q": "What is the full form of AI?",
     "options": ["A. Automated Interface", "B. Artificial Intelligence",
                 "C. Advanced Internet", "D. Auto Instruction"],
     "answer": "B", "fact": "AI enables machines to simulate human intelligence."},

    {"q": "Which symbol is used for comments in Python?",
     "options": ["A. //", "B. /*", "C. #", "D. --"],
     "answer": "C", "fact": "In Python, # starts a single-line comment."},

    {"q": "What does HTML stand for?",
     "options": ["A. Hyper Text Markup Language", "B. High Text Making Language",
                 "C. Hyper Transfer Markup Logic", "D. None of these"],
     "answer": "A", "fact": "HTML is the standard language for web pages."},

    {"q": "Which data structure works on LIFO principle?",
     "options": ["A. Queue", "B. Stack", "C. Array", "D. Tree"],
     "answer": "B", "fact": "LIFO = Last In First Out, like a stack of plates."},

    {"q": "What is the output of 2**10 in Python?",
     "options": ["A. 20", "B. 100", "C. 512", "D. 1024"],
     "answer": "D", "fact": "** is the power operator. 2^10 = 1024."},

    {"q": "Which of these is NOT a programming language?",
     "options": ["A. Python", "B. Cobra", "C. HTML", "D. Ruby"],
     "answer": "C", "fact": "HTML is a markup language, not a programming language."},
]

def main():
    print("=" * 50)
    print("         🧠  Python Quiz Game")
    print("=" * 50)
    name = input("\n  Enter your name: ").strip() or "Coder"
    print(f"\n  Welcome, {name}! Let's test your knowledge!\n")
    time.sleep(1)

    score = 0
    sample = random.sample(questions, min(7, len(questions)))

    for i, q in enumerate(sample, 1):
        print(f"\n  Q{i}. {q['q']}")
        for opt in q['options']:
            print(f"      {opt}")
        ans = input("\n  Your answer (A/B/C/D): ").strip().upper()
        if ans == q['answer']:
            print("  ✅  Correct! 🎉")
            print(f"  💡 {q['fact']}")
            score += 1
        else:
            print(f"  ❌  Wrong! Correct answer: {q['answer']}")
            print(f"  💡 {q['fact']}")
        time.sleep(0.5)

    total = len(sample)
    pct   = (score / total) * 100
    print("\n" + "=" * 50)
    print(f"  🏆  {name}'s Score: {score}/{total}  ({pct:.0f}%)")
    if pct == 100:   grade = "🔥 Perfect! You're a genius!"
    elif pct >= 70:  grade = "🌟 Great job! Keep it up!"
    elif pct >= 50:  grade = "👍 Good effort! Keep learning!"
    else:            grade = "📚 Keep studying — you'll get there!"
    print(f"  {grade}")
    print("=" * 50 + "\n")

if __name__ == "__main__":
    main()
