import tkinter as tk
from tkinter import messagebox, ttk


class ConverterApp:
    """Convert common temperatures, distances, and currencies."""

    COLORS = {
        "background": "#102a43",
        "panel": "#173f5f",
        "display": "#0b1f33",
        "text": "#f7fbff",
        "muted": "#a9c1d1",
        "accent": "#f6bd60",
        "accent_active": "#ffd58a",
        "line": "#2c5875",
    }

    CONVERSIONS = {
        "Celsius to Fahrenheit": ("Celsius", "Fahrenheit", "°C", "°F"),
        "Fahrenheit to Celsius": ("Fahrenheit", "Celsius", "°F", "°C"),
        "Km to Miles": ("Kilometers", "Miles", "km", "mi"),
        "Miles to Km": ("Miles", "Kilometers", "mi", "km"),
        "INR to USD": ("Indian Rupees", "US Dollars", "₹", "$"),
        "USD to INR": ("US Dollars", "Indian Rupees", "$", "₹"),
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Convert / Unit & Currency")
        self.root.geometry("620x590")
        self.root.minsize(500, 520)
        self.root.configure(bg=self.COLORS["background"])

        self.conversion = tk.StringVar(value="Celsius to Fahrenheit")
        self.input_value = tk.StringVar()
        self.result_text = tk.StringVar(value="Your result will appear here")
        self.detail_text = tk.StringVar(value="Select a conversion and enter a value.")
        self._configure_styles()
        self._build_layout()
        self._update_labels()

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("App.TFrame", background=self.COLORS["background"])
        style.configure("Panel.TFrame", background=self.COLORS["panel"])
        style.configure("Header.TLabel", background=self.COLORS["background"], foreground=self.COLORS["text"], font=("Segoe UI", 26, "bold"))
        style.configure("Muted.TLabel", background=self.COLORS["background"], foreground=self.COLORS["muted"], font=("Segoe UI", 10))
        style.configure("Panel.TLabel", background=self.COLORS["panel"], foreground=self.COLORS["muted"], font=("Segoe UI", 10))
        style.configure("Result.TLabel", background=self.COLORS["display"], foreground=self.COLORS["text"], font=("Segoe UI", 23, "bold"))
        style.configure("ResultMeta.TLabel", background=self.COLORS["display"], foreground=self.COLORS["accent"], font=("Segoe UI", 10))
        style.configure("Convert.TButton", background=self.COLORS["accent"], foreground=self.COLORS["display"], borderwidth=0, padding=(20, 11), font=("Segoe UI", 10, "bold"))
        style.map("Convert.TButton", background=[("active", self.COLORS["accent_active"])])
        style.configure("Reset.TButton", background=self.COLORS["line"], foreground=self.COLORS["text"], borderwidth=0, padding=(18, 11), font=("Segoe UI", 10))
        style.map("Reset.TButton", background=[("active", "#3c6b88")])

    def _build_layout(self):
        wrapper = ttk.Frame(self.root, style="App.TFrame", padding=36)
        wrapper.pack(fill="both", expand=True)
        ttk.Label(wrapper, text="CONVERT", style="Header.TLabel").pack(anchor="w")
        ttk.Label(wrapper, text="Useful conversions, all in one quiet workspace.", style="Muted.TLabel").pack(anchor="w", pady=(5, 24))

        display = tk.Frame(wrapper, bg=self.COLORS["display"], padx=22, pady=20)
        display.pack(fill="x", pady=(0, 18))
        ttk.Label(display, text="RESULT", style="ResultMeta.TLabel").pack(anchor="w")
        ttk.Label(display, textvariable=self.result_text, style="Result.TLabel", wraplength=500).pack(anchor="w", pady=(12, 7))
        ttk.Label(display, textvariable=self.detail_text, style="ResultMeta.TLabel").pack(anchor="w")

        panel = ttk.Frame(wrapper, style="Panel.TFrame", padding=24)
        panel.pack(fill="both", expand=True)
        panel.columnconfigure(0, weight=1)
        ttk.Label(panel, text="CONVERSION", style="Panel.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 6))
        menu = ttk.Combobox(panel, textvariable=self.conversion, values=list(self.CONVERSIONS), state="readonly", font=("Segoe UI", 11))
        menu.grid(row=1, column=0, sticky="ew", ipady=6, pady=(0, 18))
        menu.bind("<<ComboboxSelected>>", lambda event: self._update_labels())

        self.input_label = ttk.Label(panel, style="Panel.TLabel")
        self.input_label.grid(row=2, column=0, sticky="w", pady=(0, 6))
        entry = tk.Entry(panel, textvariable=self.input_value, bg=self.COLORS["display"], fg=self.COLORS["text"], insertbackground=self.COLORS["accent"], relief="flat", font=("Segoe UI", 13), highlightthickness=1, highlightbackground=self.COLORS["line"], highlightcolor=self.COLORS["accent"])
        entry.grid(row=3, column=0, sticky="ew", ipady=10)
        self.entry = entry

        ttk.Label(panel, text="Currency rate: 1 USD = 83.50 INR", style="Panel.TLabel").grid(row=4, column=0, sticky="w", pady=(16, 22))
        actions = ttk.Frame(panel, style="Panel.TFrame")
        actions.grid(row=5, column=0, sticky="ew")
        ttk.Button(actions, text="CONVERT", style="Convert.TButton", command=self.convert).pack(side="left")
        ttk.Button(actions, text="RESET", style="Reset.TButton", command=self.reset).pack(side="right")
        self.entry.focus_set()
        self.root.bind("<Return>", lambda event: self.convert())

    def _update_labels(self):
        source, _, source_unit, _ = self.CONVERSIONS[self.conversion.get()]
        self.input_label.config(text=f"VALUE IN {source.upper()} ({source_unit})")

    def convert(self):
        try:
            value = float(self.input_value.get())
        except ValueError:
            messagebox.showerror("Invalid value", "Enter a valid number to convert.")
            return

        conversion = self.conversion.get()
        formulas = {
            "Celsius to Fahrenheit": lambda number: number * 9 / 5 + 32,
            "Fahrenheit to Celsius": lambda number: (number - 32) * 5 / 9,
            "Km to Miles": lambda number: number * 0.621371,
            "Miles to Km": lambda number: number / 0.621371,
            "INR to USD": lambda number: number / 83.50,
            "USD to INR": lambda number: number * 83.50,
        }
        _, target, source_unit, target_unit = self.CONVERSIONS[conversion]
        result = round(formulas[conversion](value), 2)
        self.result_text.set(f"{self._format(value)} {source_unit} = {self._format(result)} {target_unit}")
        self.detail_text.set(f"Converted to {target}  /  Result type: {type(result).__name__}")

    @staticmethod
    def _format(value):
        return str(int(value)) if value.is_integer() else str(value)

    def reset(self):
        self.conversion.set("Celsius to Fahrenheit")
        self.input_value.set("")
        self.result_text.set("Your result will appear here")
        self.detail_text.set("Select a conversion and enter a value.")
        self._update_labels()
        self.entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    ConverterApp(root)
    root.mainloop()
