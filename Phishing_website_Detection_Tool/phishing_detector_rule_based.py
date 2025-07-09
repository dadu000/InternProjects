import re
import tkinter as tk
from tkinter import messagebox

# Rule-based checks
def is_suspicious(url):
    rules = [
        (lambda x: len(x) > 75, "URL is unusually long."),
        (lambda x: x.count('@') > 0, "Contains '@' symbol."),
        (lambda x: x.count('-') > 3, "Contains too many dashes."),
        (lambda x: '//' in x[7:], "Multiple '//' in the URL."),
        (lambda x: re.search(r'http[s]?://\d{1,3}(\.\d{1,3}){3}', x), "Uses IP address instead of domain."),
        (lambda x: re.search(r'login|verify|account|secure|update', x.lower()), "Suspicious keyword found.")
    ]

    for rule, reason in rules:
        if rule(url):
            return True, reason
    return False, "Looks safe."

def check_url():
    url = url_entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return
    flag, reason = is_suspicious(url)
    result_label.config(
        text=f"⚠️ Suspicious: {reason}" if flag else f"✅ Safe: {reason}",
        fg="red" if flag else "green"
    )

# GUI
root = tk.Tk()
root.title("Phishing URL Detector (Rule-Based)")
root.geometry("400x200")

tk.Label(root, text="Enter URL to check:", font=("Arial", 12)).pack(pady=10)
url_entry = tk.Entry(root, width=40)
url_entry.pack()

tk.Button(root, text="Check URL", command=check_url, bg="#2196F3", fg="white").pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
