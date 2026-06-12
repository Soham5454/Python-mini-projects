# ==================================================
#   ✅ To-Do List — Soham Dey (Soham5454)
# ==================================================

import json, os
from datetime import datetime

FILE = "todos.json"

def load():
    if os.path.exists(FILE):
        with open(FILE) as f: return json.load(f)
    return []

def save(todos):
    with open(FILE, 'w') as f: json.dump(todos, f, indent=2)

def show(todos, filter_done=None):
    items = [t for t in todos if filter_done is None or t['done'] == filter_done]
    if not items:
        print("\n  📭 No tasks found!")
        return
    print(f"\n  {'#':<4} {'Status':<8} {'Priority':<10} {'Task':<30} {'Added'}")
    print("  " + "-"*65)
    for i, t in enumerate(todos):
        if filter_done is not None and t['done'] != filter_done: continue
        status   = "✅ Done" if t['done'] else "⏳ Pending"
        priority = {"High":"🔴 High","Medium":"🟡 Medium","Low":"🟢 Low"}.get(t['priority'], t['priority'])
        print(f"  {i+1:<4} {status:<10} {priority:<12} {t['task']:<30} {t['date']}")

def add(todos):
    task = input("\n  Enter task: ").strip()
    if not task: print("  ❌ Task cannot be empty!"); return
    print("  Priority: 1.High  2.Medium  3.Low")
    p = input("  Choose (1/2/3): ").strip()
    priority = {"1":"High","2":"Medium","3":"Low"}.get(p, "Medium")
    todos.append({"task": task, "priority": priority,
                  "done": False, "date": datetime.now().strftime("%d-%m-%Y")})
    save(todos)
    print(f"  ✅ Task added with {priority} priority!")

def complete(todos):
    show(todos, filter_done=False)
    try:
        i = int(input("\n  Mark task # as done: ")) - 1
        if 0 <= i < len(todos) and not todos[i]['done']:
            todos[i]['done'] = True
            save(todos)
            print(f"  🎉 '{todos[i]['task']}' marked as done!")
        else:
            print("  ❌ Invalid or already done!")
    except ValueError:
        print("  ❌ Invalid input!")

def delete(todos):
    show(todos)
    try:
        i = int(input("\n  Delete task #: ")) - 1
        if 0 <= i < len(todos):
            removed = todos.pop(i)
            save(todos)
            print(f"  🗑️  Deleted: '{removed['task']}'")
        else:
            print("  ❌ Invalid number!")
    except ValueError:
        print("  ❌ Invalid input!")

def stats(todos):
    total   = len(todos)
    done    = sum(1 for t in todos if t['done'])
    pending = total - done
    high    = sum(1 for t in todos if t['priority']=='High' and not t['done'])
    print(f"\n  📊 Stats: Total={total}  ✅ Done={done}  ⏳ Pending={pending}  🔴 Urgent={high}")

def main():
    print("=" * 45)
    print("         ✅  To-Do List App")
    print("=" * 45)
    todos = load()
    while True:
        stats(todos)
        print("\n  1. View All Tasks     2. View Pending")
        print("  3. Add Task           4. Mark as Done")
        print("  5. Delete Task        0. Exit")
        c = input("\n  Choice: ").strip()
        if   c == '1': show(todos)
        elif c == '2': show(todos, filter_done=False)
        elif c == '3': add(todos)
        elif c == '4': complete(todos)
        elif c == '5': delete(todos)
        elif c == '0': print("\n  Stay productive! ✅\n"); break
        else: print("  ❌ Invalid choice!")

if __name__ == "__main__":
    main()
