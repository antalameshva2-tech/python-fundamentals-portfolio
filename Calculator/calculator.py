import tkinter as tk
from tkinter import messagebox, ttk


class CalculatorApp:
    """A small calculator for arithmetic and comparison operations."""

    COLORS = {
        "background": "#111827",
        "panel": "#1f2937",
        "display": "#0b1220",
        "white": "#f9fafb",
        "muted": "#9ca3af",
        "accent": "#f59e0b",
        "accent_active": "#fbbf24",
        "button": "#374151",
        "button_active": "#4b5563",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Quick Calc")
        self.root.geometry("480x620")
        self.root.minsize(400, 540)
        self.root.configure(bg=self.COLORS["background"])

        self.operator = tk.StringVar(value="+")
        self.result_text = tk.StringVar(value="Ready for a calculation")
        self.type_text = tk.StringVar(value="")
        self._configure_styles()
        self._build_layout()

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("App.TFrame", background=self.COLORS["background"])
        style.configure("Panel.TFrame", background=self.COLORS["panel"])
        style.configure("Header.TLabel", background=self.COLORS["background"], foreground=self.COLORS["white"], font=("Segoe UI", 25, "bold"))
        style.configure("Muted.TLabel", background=self.COLORS["background"], foreground=self.COLORS["muted"], font=("Segoe UI", 10))
        style.configure("PanelMuted.TLabel", background=self.COLORS["panel"], foreground=self.COLORS["muted"], font=("Segoe UI", 10))
        style.configure("Result.TLabel", background=self.COLORS["display"], foreground=self.COLORS["white"], font=("Segoe UI", 25, "bold"))
        style.configure("Type.TLabel", background=self.COLORS["display"], foreground=self.COLORS["accent"], font=("Segoe UI", 10))
        style.configure("Action.TButton", background=self.COLORS["accent"], foreground=self.COLORS["display"], borderwidth=0, padding=(20, 11), font=("Segoe UI", 10, "bold"))
        style.map("Action.TButton", background=[("active", self.COLORS["accent_active"])])
        style.configure("Clear.TButton", background=self.COLORS["button"], foreground=self.COLORS["white"], borderwidth=0, padding=(18, 11), font=("Segoe UI", 10))
        style.map("Clear.TButton", background=[("active", self.COLORS["button_active"])])

    def _build_layout(self):
        wrapper = ttk.Frame(self.root, style="App.TFrame", padding=30)
        wrapper.pack(fill="both", expand=True)
        ttk.Label(wrapper, text="QUICK CALC", style="Header.TLabel").pack(anchor="w")
        ttk.Label(wrapper, text="Arithmetic and comparisons, without the ceremony.", style="Muted.TLabel").pack(anchor="w", pady=(5, 24))

        display = tk.Frame(wrapper, bg=self.COLORS["display"], padx=22, pady=20)
        display.pack(fill="x", pady=(0, 18))
        ttk.Label(display, text="RESULT", style="Type.TLabel").pack(anchor="w")
        ttk.Label(display, textvariable=self.result_text, style="Result.TLabel", wraplength=390).pack(anchor="w", pady=(12, 5))
        ttk.Label(display, textvariable=self.type_text, style="Type.TLabel").pack(anchor="w")

        panel = ttk.Frame(wrapper, style="Panel.TFrame", padding=22)
        panel.pack(fill="both", expand=True)
        panel.columnconfigure(0, weight=1)
        panel.columnconfigure(1, weight=1)
        panel.columnconfigure(2, weight=1)

        ttk.Label(panel, text="FIRST NUMBER", style="PanelMuted.TLabel").grid(row=0, column=0, columnspan=3, sticky="w", pady=(0, 6))
        self.first_number = self._entry(panel)
        self.first_number.grid(row=1, column=0, columnspan=3, sticky="ew", ipady=9, pady=(0, 18))
        ttk.Label(panel, text="OPERATOR", style="PanelMuted.TLabel").grid(row=2, column=0, sticky="w", pady=(0, 6))
        ttk.Label(panel, text="SECOND NUMBER", style="PanelMuted.TLabel").grid(row=2, column=1, columnspan=2, sticky="w", padx=(14, 0), pady=(0, 6))
        operators = ["+", "-", "*", "/", "%", "//", "**", ">", "<", "=="]
        operator_menu = ttk.Combobox(panel, textvariable=self.operator, values=operators, state="readonly", font=("Segoe UI", 12))
        operator_menu.grid(row=3, column=0, sticky="ew", ipady=5)
        self.second_number = self._entry(panel)
        self.second_number.grid(row=3, column=1, columnspan=2, sticky="ew", ipady=9, padx=(14, 0))

        hint = "Supported:  +   -   *   /   %   //   **   >   <   =="
        ttk.Label(panel, text=hint, style="PanelMuted.TLabel").grid(row=4, column=0, columnspan=3, sticky="w", pady=(18, 22))
        actions = ttk.Frame(panel, style="Panel.TFrame")
        actions.grid(row=5, column=0, columnspan=3, sticky="ew")
        ttk.Button(actions, text="CALCULATE", style="Action.TButton", command=self.calculate).pack(side="left")
        ttk.Button(actions, text="CLEAR", style="Clear.TButton", command=self.clear).pack(side="right")
        self.first_number.focus_set()
        self.root.bind("<Return>", lambda event: self.calculate())

    def _entry(self, parent):
        return tk.Entry(parent, bg=self.COLORS["display"], fg=self.COLORS["white"], insertbackground=self.COLORS["accent"], relief="flat", font=("Segoe UI", 12), highlightthickness=1, highlightbackground=self.COLORS["button"], highlightcolor=self.COLORS["accent"])

    def calculate(self):
        try:
            first = float(self.first_number.get())
            second = float(self.second_number.get())
        except ValueError:
            messagebox.showerror("Invalid number", "Enter a valid number in both fields.")
            return

        operator = self.operator.get()
        if operator in ("/", "%", "//") and second == 0:
            messagebox.showerror("Cannot calculate", "Division by zero is not allowed.")
            return
        operations = {
            "+": lambda: first + second,
            "-": lambda: first - second,
            "*": lambda: first * second,
            "/": lambda: first / second,
            "%": lambda: first % second,
            "//": lambda: int(first // second),
            "**": lambda: first ** second,
            ">": lambda: first > second,
            "<": lambda: first < second,
            "==": lambda: first == second,
        }
        try:
            result = operations[operator]()
        except (OverflowError, ZeroDivisionError):
            messagebox.showerror("Calculation error", "Those values cannot be calculated safely.")
            return
        self.result_text.set(f"{self._format(first)} {operator} {self._format(second)} = {self._format(result)}")
        self.type_text.set(f"Result type: {type(result).__name__}")

    @staticmethod
    def _format(value):
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    def clear(self):
        self.first_number.delete(0, tk.END)
        self.second_number.delete(0, tk.END)
        self.operator.set("+")
        self.result_text.set("Ready for a calculation")
        self.type_text.set("")
        self.first_number.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    CalculatorApp(root)
    root.mainloop()