import tkinter as tk
from tkinter import messagebox, ttk


class CardGeneratorApp:
    """Desktop interface for creating a personal introduction card."""

    COLORS = {
        "background": "#101820",
        "panel": "#17232d",
        "card": "#f4f0e8",
        "ink": "#18232b",
        "muted": "#9eabb4",
        "white": "#ffffff",
        "coral": "#ff8066",
        "mint": "#a6e3c4",
        "line": "#2b3a45",
    }

    def __init__(self, root):
        self.root = root
        self.root.title("Personal Introduction Card")
        self.root.geometry("980x650")
        self.root.minsize(820, 560)
        self.root.configure(bg=self.COLORS["background"])

        self.fields = {}
        self._configure_styles()
        self._build_layout()

    def _configure_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "App.TFrame", background=self.COLORS["background"]
        )
        style.configure(
            "Panel.TFrame", background=self.COLORS["panel"]
        )
        style.configure(
            "Field.TLabel",
            background=self.COLORS["panel"],
            foreground=self.COLORS["muted"],
            font=("Segoe UI", 10),
        )
        style.configure(
            "Title.TLabel",
            background=self.COLORS["background"],
            foreground=self.COLORS["white"],
            font=("Georgia", 27, "bold"),
        )
        style.configure(
            "Subtitle.TLabel",
            background=self.COLORS["background"],
            foreground=self.COLORS["muted"],
            font=("Segoe UI", 11),
        )
        style.configure(
            "Generate.TButton",
            background=self.COLORS["coral"],
            foreground=self.COLORS["ink"],
            borderwidth=0,
            padding=(18, 11),
            font=("Segoe UI", 10, "bold"),
        )
        style.map("Generate.TButton", background=[("active", "#ff9b84")])
        style.configure(
            "Reset.TButton",
            background=self.COLORS["line"],
            foreground=self.COLORS["white"],
            borderwidth=0,
            padding=(14, 11),
            font=("Segoe UI", 10),
        )
        style.map("Reset.TButton", background=[("active", "#3b4d5a")])

    def _build_layout(self):
        wrapper = ttk.Frame(self.root, style="App.TFrame", padding=42)
        wrapper.pack(fill="both", expand=True)

        header = ttk.Frame(wrapper, style="App.TFrame")
        header.pack(fill="x", pady=(0, 30))
        ttk.Label(header, text="MAKE IT PERSONAL", style="Title.TLabel").pack(
            anchor="w"
        )
        ttk.Label(
            header,
            text="Build a card that introduces you at a glance.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(6, 0))

        content = ttk.Frame(wrapper, style="App.TFrame")
        content.pack(fill="both", expand=True)
        content.columnconfigure(0, weight=2)
        content.columnconfigure(1, weight=3)
        content.rowconfigure(0, weight=1)

        form = ttk.Frame(content, style="Panel.TFrame", padding=28)
        form.grid(row=0, column=0, sticky="nsew", padx=(0, 18))
        form.columnconfigure(0, weight=1)

        ttk.Label(form, text="YOUR DETAILS", style="Field.TLabel").grid(
            row=0, column=0, sticky="w", pady=(0, 20)
        )
        field_definitions = [
            ("Name", "Your name"),
            ("Age", "Your age"),
            ("City", "Where you live"),
            ("Hobby", "What you enjoy"),
            ("Language", "Favorite programming language"),
        ]
        for row, (label, placeholder) in enumerate(field_definitions, start=1):
            ttk.Label(form, text=label.upper(), style="Field.TLabel").grid(
                row=row * 2 - 1, column=0, sticky="w", pady=(0, 5)
            )
            entry = tk.Entry(
                form,
                bg=self.COLORS["background"],
                fg=self.COLORS["white"],
                insertbackground=self.COLORS["coral"],
                relief="flat",
                font=("Segoe UI", 11),
                highlightthickness=1,
                highlightbackground=self.COLORS["line"],
                highlightcolor=self.COLORS["coral"],
            )
            entry.insert(0, placeholder)
            entry.bind("<FocusIn>", lambda event, field=entry, text=placeholder: self._clear_placeholder(field, text))
            entry.bind("<FocusOut>", lambda event, field=entry, text=placeholder: self._restore_placeholder(field, text))
            entry.grid(row=row * 2, column=0, sticky="ew", ipady=9, pady=(0, 13))
            self.fields[label] = (entry, placeholder)

        actions = ttk.Frame(form, style="Panel.TFrame")
        actions.grid(row=12, column=0, sticky="ew", pady=(8, 0))
        ttk.Button(actions, text="GENERATE CARD", style="Generate.TButton", command=self.generate_card).pack(side="left")
        ttk.Button(actions, text="RESET", style="Reset.TButton", command=self.reset).pack(side="right")

        preview = tk.Frame(content, bg=self.COLORS["card"], padx=34, pady=30)
        preview.grid(row=0, column=1, sticky="nsew")
        self.preview = preview
        self.card_title = tk.Label(preview, text="PERSONAL INTRODUCTION", bg=self.COLORS["card"], fg=self.COLORS["coral"], font=("Segoe UI", 10, "bold"))
        self.card_title.pack(anchor="w")
        tk.Frame(preview, bg=self.COLORS["coral"], height=3, width=68).pack(anchor="w", pady=(12, 32))
        self.card_name = tk.Label(preview, text="Your name", bg=self.COLORS["card"], fg=self.COLORS["ink"], font=("Georgia", 28, "bold"), wraplength=420, justify="left")
        self.card_name.pack(anchor="w")
        self.card_details = tk.Label(preview, text="Fill in your details, then generate your card.", bg=self.COLORS["card"], fg="#52616b", font=("Segoe UI", 12), justify="left", anchor="nw")
        self.card_details.pack(anchor="w", pady=(24, 0))
        self.card_status = tk.Label(preview, text="", bg=self.COLORS["card"], fg="#42735a", font=("Segoe UI", 11, "bold"), justify="left")
        self.card_status.pack(anchor="w", pady=(28, 0))
        ttk.Button(preview, text="COPY CARD TEXT", style="Reset.TButton", command=self.copy_card).pack(anchor="w", side="bottom")

    @staticmethod
    def _clear_placeholder(entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)

    @staticmethod
    def _restore_placeholder(entry, placeholder):
        if not entry.get().strip():
            entry.insert(0, placeholder)

    def _value(self, label):
        entry, placeholder = self.fields[label]
        value = entry.get().strip()
        return "" if value == placeholder else value

    def generate_card(self):
        values = {label: self._value(label) for label in self.fields}
        if any(not value for value in values.values()):
            messagebox.showwarning("Missing details", "Please complete every field before generating your card.")
            return
        try:
            age = int(values["Age"])
            if age < 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid age", "Age must be a whole number greater than or equal to 0.")
            return

        self.card_name.config(text=values["Name"])
        self.card_details.config(
            text=f"AGE     {age}\n\nCITY     {values['City']}\n\nHOBBY    {values['Hobby']}\n\nLANGUAGE  {values['Language']}"
        )
        self.card_status.config(
            text="ELIGIBLE TO VOTE" if age >= 18 else "NOT ELIGIBLE TO VOTE",
            fg="#42735a" if age >= 18 else "#b25b4b",
        )

    def copy_card(self):
        name = self.card_name.cget("text")
        details = self.card_details.cget("text")
        status = self.card_status.cget("text")
        if name == "Your name":
            messagebox.showinfo("Nothing to copy", "Generate your card first.")
            return
        self.root.clipboard_clear()
        self.root.clipboard_append(f"PERSONAL INTRODUCTION\n\n{name}\n\n{details}\n\n{status}")
        messagebox.showinfo("Copied", "Your card text is ready to paste.")

    def reset(self):
        for entry, placeholder in self.fields.values():
            entry.delete(0, tk.END)
            entry.insert(0, placeholder)
        self.card_name.config(text="Your name")
        self.card_details.config(text="Fill in your details, then generate your card.")
        self.card_status.config(text="", fg="#42735a")


if __name__ == "__main__":
    root = tk.Tk()
    CardGeneratorApp(root)
    root.mainloop()