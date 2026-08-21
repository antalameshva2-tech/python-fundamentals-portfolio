import tkinter as tk
from tkinter import messagebox, ttk

CONVERSIONS = {
    "Celsius to Fahrenheit": {
        "from": "Celsius",
        "to": "Fahrenheit",
        "suffix": "C",
        "target_suffix": "F",
        "calculate": lambda value: (value * 9 / 5) + 32,
    },
    "Kilometers to Miles": {
        "from": "Kilometers",
        "to": "Miles",
        "suffix": "km",
        "target_suffix": "mi",
        "calculate": lambda value: value * 0.621371,
    },
    "INR to USD": {
        "from": "Indian Rupees",
        "to": "US Dollars",
        "suffix": "INR",
        "target_suffix": "USD",
        "calculate": lambda value: value * 0.012,
    },
}

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Convertly | Unit and Currency Converter")
        self.root.geometry("620x690")
        self.root.minsize(520, 620)
        self.root.configure(bg="#eef3f7")

        self.conversion_var = tk.StringVar(value="Celsius to Fahrenheit")
        self.value_var = tk.StringVar()
        self.result_var = tk.StringVar(value="0.00")
        self.formula_var = tk.StringVar(value="Choose a conversion to get started")
        self.status_var = tk.StringVar(value="Ready")

        self.setup_styles()
        self.build_ui()
        self.value_var.trace_add("write", self.update_preview)

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("App.TFrame", background="#eef3f7")
        style.configure("Card.TFrame", background="#ffffff")
        style.configure("Title.TLabel", background="#1e3a46", foreground="#ffffff",
                        font=("Segoe UI", 27, "bold"))
        style.configure("Subtitle.TLabel", background="#1e3a46", foreground="#b9d8d1",
                        font=("Segoe UI", 11))
        style.configure("Section.TLabel", background="#ffffff", foreground="#1e3a46",
                        font=("Segoe UI", 11, "bold"))
        style.configure("Muted.TLabel", background="#ffffff", foreground="#71818a",
                        font=("Segoe UI", 10))
        style.configure("Value.TLabel", background="#ffffff", foreground="#1e3a46",
                        font=("Segoe UI", 30, "bold"))
        style.configure("Accent.TButton", background="#e07a5f", foreground="#ffffff",
                        font=("Segoe UI", 10, "bold"), padding=(18, 10), borderwidth=0)
        style.map("Accent.TButton", background=[("active", "#c9664d")])
        style.configure("Secondary.TButton", background="#e8eef0", foreground="#1e3a46",
                        font=("Segoe UI", 10, "bold"), padding=(14, 10), borderwidth=0)
        style.map("Secondary.TButton", background=[("active", "#d6e2e5")])
        style.configure("TCombobox", padding=8, fieldbackground="#f7fafb")
        style.configure("Input.TEntry", padding=10, font=("Segoe UI", 13))

    def build_ui(self):
        main = ttk.Frame(self.root, style="App.TFrame", padding=26)
        main.pack(fill=tk.BOTH, expand=True)

        header = tk.Frame(main, bg="#1e3a46", padx=26, pady=24)
        header.pack(fill=tk.X)
        ttk.Label(header, text="Convertly", style="Title.TLabel").pack(anchor=tk.W)
        ttk.Label(header, text="Simple conversions, clearly shown.", style="Subtitle.TLabel").pack(
            anchor=tk.W, pady=(4, 0)
        )

        card = ttk.Frame(main, style="Card.TFrame", padding=26)
        card.pack(fill=tk.BOTH, expand=True, pady=(18, 0))

        ttk.Label(card, text="CONVERSION", style="Muted.TLabel").pack(anchor=tk.W)
        self.conversion_box = ttk.Combobox(
            card, textvariable=self.conversion_var, values=list(CONVERSIONS),
            state="readonly", font=("Segoe UI", 11)
        )
        self.conversion_box.pack(fill=tk.X, pady=(7, 24))
        self.conversion_box.bind("<<ComboboxSelected>>", self.update_labels)

        self.input_label = ttk.Label(card, text="Temperature", style="Section.TLabel")
        self.input_label.pack(anchor=tk.W)
        input_row = ttk.Frame(card, style="Card.TFrame")
        input_row.pack(fill=tk.X, pady=(7, 14))
        self.input_entry = ttk.Entry(input_row, textvariable=self.value_var, style="Input.TEntry")
        self.input_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.unit_label = ttk.Label(input_row, text="C", style="Section.TLabel", width=5,
                                    anchor=tk.CENTER)
        self.unit_label.pack(side=tk.LEFT, padx=(10, 0))

        buttons = ttk.Frame(card, style="Card.TFrame")
        buttons.pack(fill=tk.X, pady=(2, 25))
        ttk.Button(buttons, text="Convert", command=self.convert, style="Accent.TButton").pack(
            side=tk.LEFT, fill=tk.X, expand=True
        )
        ttk.Button(buttons, text="Clear", command=self.clear, style="Secondary.TButton").pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0)
        )

        result_panel = tk.Frame(card, bg="#f2f7f6", padx=18, pady=16)
        result_panel.pack(fill=tk.X)
        ttk.Label(result_panel, text="RESULT", style="Muted.TLabel").pack(anchor=tk.W)
        ttk.Label(result_panel, textvariable=self.result_var, style="Value.TLabel").pack(
            anchor=tk.W, pady=(3, 0)
        )
        ttk.Label(result_panel, textvariable=self.formula_var, style="Muted.TLabel").pack(
            anchor=tk.W, pady=(3, 0)
        )

        footer = ttk.Frame(card, style="Card.TFrame")
        footer.pack(fill=tk.X, pady=(18, 0))
        ttk.Label(footer, textvariable=self.status_var, style="Muted.TLabel").pack(side=tk.LEFT)
        ttk.Label(footer, text="INR rate: 0.012 USD", style="Muted.TLabel").pack(side=tk.RIGHT)
        self.input_entry.focus_set()

    def update_labels(self, _event=None):
        conversion = CONVERSIONS[self.conversion_var.get()]
        self.input_label.config(text=f"Amount in {conversion['from']}")
        self.unit_label.config(text=conversion["suffix"])
        self.result_var.set("0.00")
        self.formula_var.set(f"{conversion['from']} -> {conversion['to']}")
        self.status_var.set("Ready")

    def update_preview(self, *_args):
        if not self.value_var.get().strip():
            self.status_var.set("Ready")

    def convert(self):
        raw_value = self.value_var.get().strip()
        if not raw_value:
            messagebox.showwarning("Missing value", "Enter a number to convert.")
            self.input_entry.focus_set()
            return

        try:
            value = float(raw_value)
        except ValueError:
            messagebox.showerror("Invalid value", "Please enter a valid number.")
            self.input_entry.focus_set()
            return

        conversion = CONVERSIONS[self.conversion_var.get()]
        old_id = id(value)
        result = conversion["calculate"](value)
        new_id = id(result)
        self.result_var.set(f"{result:,.2f} {conversion['target_suffix']}")
        self.formula_var.set(
            f"{value:,.2f} {conversion['suffix']} = {result:,.2f} {conversion['target_suffix']}"
        )
        self.status_var.set(f"Converted successfully  |  value id: {old_id}  result id: {new_id}")

    def clear(self):
        self.value_var.set("")
        self.result_var.set("0.00")
        self.formula_var.set("Choose a conversion to get started")
        self.status_var.set("Ready")
        self.input_entry.focus_set()


def main():
    root = tk.Tk()
    ConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
