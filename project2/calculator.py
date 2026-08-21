import tkinter as tk
from tkinter import ttk


def calculate(num1, num2, operator):
    """Return the result for one supported operation."""
    if operator == "+":
        return num1 + num2
    if operator == "-":
        return num1 - num2
    if operator == "*":
        return num1 * num2
    if operator == "/":
        return num1 / num2
    if operator == "%":
        return num1 % num2
    if operator == "//":
        return num1 // num2
    if operator == "**":
        return num1**num2
    raise ValueError("Invalid operator")


def show_result():
    try:
        num1 = float(first_number.get())
        num2 = float(second_number.get())
        operator = operation.get()

        if operator in {"/", "%", "//"} and num2 == 0:
            raise ZeroDivisionError

        result = calculate(num1, num2, operator)
        result_text.set(f"{num1:g} {operator} {num2:g} = {result:g}")
        status_text.set(f"Result type: {type(result).__name__}")
        result_label.configure(foreground="#1f7a55")
    except ValueError:
        result_text.set("Please enter valid numbers")
        status_text.set("Use numeric values such as 12 or 3.5")
        result_label.configure(foreground="#b54747")
    except ZeroDivisionError:
        result_text.set("Cannot divide by zero")
        status_text.set("Choose a non-zero second number")
        result_label.configure(foreground="#b54747")


def clear_fields():
    first_number.set("")
    second_number.set("")
    operation.set("+")
    result_text.set("Your result will appear here")
    status_text.set("Ready")
    result_label.configure(foreground="#244052")


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("820x470")
root.minsize(700, 430)
root.configure(background="#f3f6f5")

style = ttk.Style(root)
style.theme_use("clam")
style.configure("TLabel", background="#f3f6f5", foreground="#244052", font=("Segoe UI", 11))
style.configure("Title.TLabel", font=("Segoe UI", 25, "bold"), foreground="#183746")
style.configure("Subtitle.TLabel", font=("Segoe UI", 10), foreground="#61747a")
style.configure("TEntry", padding=10, font=("Segoe UI", 12))
style.configure("TCombobox", padding=8, font=("Segoe UI", 12))
style.configure("Accent.TButton", padding=11, font=("Segoe UI", 11, "bold"), foreground="white", background="#167d68")
style.map("Accent.TButton", background=[("active", "#126654")])
style.configure("Clear.TButton", padding=11, font=("Segoe UI", 11), foreground="#244052", background="#dce8e4")

first_number = tk.StringVar()
second_number = tk.StringVar()
operation = tk.StringVar(value="+")
result_text = tk.StringVar(value="Your result will appear here")
status_text = tk.StringVar(value="Ready")

content = ttk.Frame(root, padding=32)
content.pack(fill="both", expand=True)
ttk.Label(content, text="Calculator", style="Title.TLabel").pack(anchor="w")
ttk.Label(content, text="Quick, clear arithmetic for everyday work", style="Subtitle.TLabel").pack(anchor="w", pady=(4, 24))

workspace = ttk.Frame(content)
workspace.pack(fill="both", expand=True)
workspace.columnconfigure(0, weight=1)
workspace.columnconfigure(1, weight=1)
workspace.rowconfigure(0, weight=1)

form = ttk.Frame(workspace, padding=(0, 0, 24, 0))
form.grid(row=0, column=0, sticky="nsew")

ttk.Label(form, text="First number").pack(anchor="w")
ttk.Entry(form, textvariable=first_number).pack(fill="x", pady=(6, 18))

ttk.Label(form, text="Operation").pack(anchor="w")
ttk.Combobox(form, textvariable=operation, values=["+", "-", "*", "/", "%", "//", "**"], state="readonly").pack(fill="x", pady=(6, 18))

ttk.Label(form, text="Second number").pack(anchor="w")
ttk.Entry(form, textvariable=second_number).pack(fill="x", pady=(6, 24))

buttons = ttk.Frame(form)
buttons.pack(fill="x")
ttk.Button(buttons, text="Calculate", style="Accent.TButton", command=show_result).pack(side="left", fill="x", expand=True, padx=(0, 6))
ttk.Button(buttons, text="Clear", style="Clear.TButton", command=clear_fields).pack(side="left", fill="x", expand=True, padx=(6, 0))

result_panel = tk.Frame(workspace, background="#e4efeb", padx=24, pady=24)
result_panel.grid(row=0, column=1, sticky="nsew")
tk.Label(result_panel, text="OUTPUT", background="#e4efeb", foreground="#61747a", font=("Segoe UI", 10, "bold")).pack(anchor="w")
result_label = tk.Label(result_panel, textvariable=result_text, background="#e4efeb", foreground="#244052", font=("Segoe UI", 18, "bold"), justify="left", wraplength=300)
result_label.pack(anchor="w", pady=(32, 12))
tk.Label(result_panel, textvariable=status_text, background="#e4efeb", foreground="#61747a", font=("Segoe UI", 10), justify="left", wraplength=300).pack(anchor="w")

root.bind("<Return>", lambda _event: show_result())
root.mainloop()