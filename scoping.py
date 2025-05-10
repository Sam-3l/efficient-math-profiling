"""
🔍 Scoping in Python – What Is It?
Scoping defines where variables are accessible in your code.

Python uses the LEGB rule for variable lookup:

L: Local — inside a function.

E: Enclosing — function inside another function.

G: Global — top-level of script/module.

B: Built-in — preloaded names like len, print.

🧠 Stacks – What Are They?
A stack is a data structure where Python keeps track of function calls (called the call stack).
It’s Last-In-First-Out (LIFO) — the last function called is the first to finish.

🧪 Code Example — Scoping + Stack in Action
Let’s look at Example 4.5-style code:
"""

def outer():
    x = "enclosed"

    def inner():
        x = "local"
        print("Inner x:", x)

    inner()
    print("Outer x:", x)

x = "global"
outer()
print("Global x:", x)
