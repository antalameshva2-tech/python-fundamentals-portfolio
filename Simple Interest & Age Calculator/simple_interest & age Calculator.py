# ==========================================
# PART A: Simple & Compound Interest Calculator
# ==========================================

import tkinter as tk
from datetime import date
from tkinter import messagebox, ttk


class InterestAgeApp:
	COLORS = {
		"background": "#15202b",
		"panel": "#203445",
		"display": "#0d1822",
		"text": "#f5f7fa",
		"muted": "#a6b8c5",
		"accent": "#73d2a5",
		"accent_active": "#91e4bc",
		"line": "#345267",
		"secondary": "#e9b872",
	}

	def __init__(self, root):
		self.root = root
		self.root.title("Interest & Age Calculator")
		self.root.geometry("720x620")
		self.root.minsize(580, 540)
		self.root.configure(bg=self.COLORS["background"])
		self.interest_entries = {}
		self._configure_styles()
		self._build_layout()

	def _configure_styles(self):
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("App.TFrame", background=self.COLORS["background"])
		style.configure("Panel.TFrame", background=self.COLORS["panel"])
		style.configure("Header.TLabel", background=self.COLORS["background"], foreground=self.COLORS["text"], font=("Segoe UI", 27, "bold"))
		style.configure("Subtitle.TLabel", background=self.COLORS["background"], foreground=self.COLORS["muted"], font=("Segoe UI", 10))
		style.configure("Tab.TNotebook", background=self.COLORS["background"], borderwidth=0)
		style.configure("Tab.TNotebook.Tab", background=self.COLORS["panel"], foreground=self.COLORS["muted"], padding=(20, 10), font=("Segoe UI", 10, "bold"))
		style.map("Tab.TNotebook.Tab", background=[("selected", self.COLORS["accent"])], foreground=[("selected", self.COLORS["display"])])
		style.configure("Field.TLabel", background=self.COLORS["panel"], foreground=self.COLORS["muted"], font=("Segoe UI", 10))
		style.configure("ResultLabel.TLabel", background=self.COLORS["display"], foreground=self.COLORS["text"], font=("Segoe UI", 22, "bold"))
		style.configure("ResultMeta.TLabel", background=self.COLORS["display"], foreground=self.COLORS["accent"], font=("Segoe UI", 10))
		style.configure("Action.TButton", background=self.COLORS["accent"], foreground=self.COLORS["display"], borderwidth=0, padding=(18, 11), font=("Segoe UI", 10, "bold"))
		style.map("Action.TButton", background=[("active", self.COLORS["accent_active"])])
		style.configure("Reset.TButton", background=self.COLORS["line"], foreground=self.COLORS["text"], borderwidth=0, padding=(17, 11), font=("Segoe UI", 10))
		style.map("Reset.TButton", background=[("active", "#466a80")])

	def _build_layout(self):
		wrapper = ttk.Frame(self.root, style="App.TFrame", padding=38)
		wrapper.pack(fill="both", expand=True)
		ttk.Label(wrapper, text="CALCULATE WITH CLARITY", style="Header.TLabel").pack(anchor="w")
		ttk.Label(wrapper, text="Interest projections and age, gathered in one simple tool.", style="Subtitle.TLabel").pack(anchor="w", pady=(5, 25))

		notebook = ttk.Notebook(wrapper, style="Tab.TNotebook")
		notebook.pack(fill="both", expand=True)
		interest_tab = ttk.Frame(notebook, style="Panel.TFrame", padding=26)
		age_tab = ttk.Frame(notebook, style="Panel.TFrame", padding=26)
		notebook.add(interest_tab, text="  INTEREST  ")
		notebook.add(age_tab, text="  AGE  ")
		self._build_interest_tab(interest_tab)
		self._build_age_tab(age_tab)

	def _entry(self, parent):
		return tk.Entry(parent, bg=self.COLORS["display"], fg=self.COLORS["text"], insertbackground=self.COLORS["accent"], relief="flat", font=("Segoe UI", 12), highlightthickness=1, highlightbackground=self.COLORS["line"], highlightcolor=self.COLORS["accent"])

	def _build_interest_tab(self, parent):
		parent.columnconfigure(0, weight=1)
		parent.columnconfigure(1, weight=1)
		fields = (("Principal amount", "principal"), ("Rate of interest (%)", "rate"), ("Time period (years)", "time"))
		for column, (label, key) in enumerate(fields):
			ttk.Label(parent, text=label.upper(), style="Field.TLabel").grid(row=0, column=column, sticky="w", padx=(0, 12) if column < 2 else 0, pady=(0, 7))
			entry = self._entry(parent)
			entry.grid(row=1, column=column, sticky="ew", padx=(0, 12) if column < 2 else 0, ipady=9)
			self.interest_entries[key] = entry

		display = tk.Frame(parent, bg=self.COLORS["display"], padx=22, pady=20)
		display.grid(row=3, column=0, columnspan=2, sticky="nsew", pady=(28, 20))
		parent.rowconfigure(3, weight=1)
		ttk.Label(display, text="INTEREST SUMMARY", style="ResultMeta.TLabel").pack(anchor="w")
		self.interest_result = ttk.Label(display, text="Enter your values to see the projection", style="ResultLabel.TLabel", wraplength=550)
		self.interest_result.pack(anchor="w", pady=(13, 8))
		self.interest_detail = ttk.Label(display, text="Simple interest  /  Compound interest  /  Difference", style="ResultMeta.TLabel")
		self.interest_detail.pack(anchor="w")

		actions = ttk.Frame(parent, style="Panel.TFrame")
		actions.grid(row=4, column=0, columnspan=2, sticky="ew")
		ttk.Button(actions, text="CALCULATE INTEREST", style="Action.TButton", command=self.calculate_interest).pack(side="left")
		ttk.Button(actions, text="RESET", style="Reset.TButton", command=self.reset_interest).pack(side="right")
		self.interest_entries["principal"].focus_set()

	def _build_age_tab(self, parent):
		parent.columnconfigure(0, weight=1)
		ttk.Label(parent, text="BIRTH YEAR", style="Field.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 7))
		self.birth_year = self._entry(parent)
		self.birth_year.grid(row=1, column=0, sticky="ew", ipady=9)
		display = tk.Frame(parent, bg=self.COLORS["display"], padx=22, pady=20)
		display.grid(row=3, column=0, sticky="nsew", pady=(28, 20))
		parent.rowconfigure(3, weight=1)
		ttk.Label(display, text="AGE SUMMARY", style="ResultMeta.TLabel").pack(anchor="w")
		self.age_result = ttk.Label(display, text="Enter a birth year to calculate age", style="ResultLabel.TLabel", wraplength=550)
		self.age_result.pack(anchor="w", pady=(13, 8))
		self.age_detail = ttk.Label(display, text=f"Age is calculated for the current year: {date.today().year}", style="ResultMeta.TLabel")
		self.age_detail.pack(anchor="w")
		actions = ttk.Frame(parent, style="Panel.TFrame")
		actions.grid(row=4, column=0, sticky="ew")
		ttk.Button(actions, text="CALCULATE AGE", style="Action.TButton", command=self.calculate_age).pack(side="left")
		ttk.Button(actions, text="RESET", style="Reset.TButton", command=self.reset_age).pack(side="right")
		self.birth_year.focus_set()

	def calculate_interest(self):
		try:
			principal = float(self.interest_entries["principal"].get())
			rate = float(self.interest_entries["rate"].get())
			time = float(self.interest_entries["time"].get())
			if principal < 0 or rate < 0 or time < 0:
				raise ValueError
		except ValueError:
			messagebox.showerror("Invalid values", "Enter non-negative numbers for all interest fields.")
			return
		simple_interest = principal * rate * time / 100
		compound_interest = principal * ((1 + rate / 100) ** time) - principal
		difference = compound_interest - simple_interest
		self.interest_result.config(text=f"Simple: Rs. {simple_interest:.2f}    Compound: Rs. {compound_interest:.2f}")
		self.interest_detail.config(text=f"Difference (compound - simple): Rs. {difference:.2f}")

	def calculate_age(self):
		try:
			birth_year = int(self.birth_year.get())
			current_year = date.today().year
			if birth_year > current_year or birth_year < 0:
				raise ValueError
		except ValueError:
			messagebox.showerror("Invalid birth year", "Enter a valid year up to the current year.")
			return
		age = date.today().year - birth_year
		self.age_result.config(text=f"You are {age} years old")
		self.age_detail.config(text=f"Based on birth year {birth_year} and current year {date.today().year}")

	def reset_interest(self):
		for entry in self.interest_entries.values():
			entry.delete(0, tk.END)
		self.interest_result.config(text="Enter your values to see the projection")
		self.interest_detail.config(text="Simple interest  /  Compound interest  /  Difference")
		self.interest_entries["principal"].focus_set()

	def reset_age(self):
		self.birth_year.delete(0, tk.END)
		self.age_result.config(text="Enter a birth year to calculate age")
		self.age_detail.config(text=f"Age is calculated for the current year: {date.today().year}")
		self.birth_year.focus_set()


if __name__ == "__main__":
	root = tk.Tk()
	InterestAgeApp(root)
	root.mainloop()