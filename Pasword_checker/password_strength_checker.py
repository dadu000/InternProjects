import tkinter as tk
from tkinter import messagebox
import re

try:
    import nltk
    from nltk.corpus import words
    nltk.download('words')
    nltk_words = set(words.words())
    NLTK_AVAILABLE = True
except:
    NLTK_AVAILABLE = False

def check_strength(password):
    suggestions = []
    score = 0

    if len(password) < 8:
        suggestions.append("Use at least 8 characters.")
    else:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add a digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        suggestions.append("Add a special character (!, @, #, etc).")

    if NLTK_AVAILABLE:
        if password.lower() in nltk_words:
            suggestions.append("Avoid common dictionary words.")
            score -= 1

    if score <= 2:
        strength = "Weak"
        color = "red"
    elif score == 3 or score == 4:
        strength = "Medium"
        color = "orange"
    else:
        strength = "Strong"
        color = "green"

    return strength, suggestions, color

def analyze_password():
    pwd = entry.get()
    strength, suggestions, color = check_strength(pwd)
    result_label.config(text=f"Password Strength: {strength}", fg=color)

    if suggestions:
        suggest_text = "\n".join(f"- {s}" for s in suggestions)
    else:
        suggest_text = "Your password looks strong!"
    
    suggestions_label.config(text=suggest_text)

# GUI Setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Check Strength", command=analyze_password, font=("Arial", 12), bg="#4CAF50", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=5)

suggestions_label = tk.Label(root, text="", font=("Arial", 10), justify="left", wraplength=350)
suggestions_label.pack(pady=10)

root.mainloop()
