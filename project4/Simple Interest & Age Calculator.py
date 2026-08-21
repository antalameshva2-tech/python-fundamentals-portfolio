import tkinter as tk
from datetime import date
from tkinter import messagebox, ttk


class CalculatorApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Calcwise | Interest and Age")
		self.root.geometry("650x650")
		self.root.minsize(560, 580)
		self.root.configure(bg="#eef3f7")

		self.principal_var = tk.StringVar()
		self.rate_var = tk.StringVar()
		self.time_var = tk.StringVar()
		self.birth_year_var = tk.StringVar()
		self.interest_result_var = tk.StringVar(value="Rs. 0.00")
		self.age_result_var = tk.StringVar(value="0 years")
		self.interest_status_var = tk.StringVar(value="Enter the values to calculate interest")
		self.age_status_var = tk.StringVar(value="Enter your birth year")

		self.setup_styles()
		self.build_ui()

	def setup_styles(self):
		style = ttk.Style()
		style.theme_use("clam")
		style.configure("App.TFrame", background="#eef3f7")
		style.configure("Card.TFrame", background="#ffffff")
		style.configure("Header.TFrame", background="#203a43")
		style.configure("Title.TLabel", background="#203a43", foreground="#ffffff",
						font=("Segoe UI", 27, "bold"))
		style.configure("Subtitle.TLabel", background="#203a43", foreground="#b9d8d1",
						font=("Segoe UI", 11))
		style.configure("Label.TLabel", background="#ffffff", foreground="#203a43",
						font=("Segoe UI", 10, "bold"))
		style.configure("Muted.TLabel", background="#ffffff", foreground="#71818a",
						font=("Segoe UI", 10))
		style.configure("Result.TLabel", background="#f2f7f6", foreground="#203a43",
						font=("Segoe UI", 28, "bold"))
		style.configure("ResultPanel.TLabel", background="#f2f7f6", foreground="#71818a",
						font=("Segoe UI", 10))
		style.configure("Accent.TButton", background="#e07a5f", foreground="#ffffff",
						font=("Segoe UI", 10, "bold"), padding=(18, 10), borderwidth=0)
		style.map("Accent.TButton", background=[("active", "#c9664d")])
		style.configure("Secondary.TButton", background="#e8eef0", foreground="#203a43",
						font=("Segoe UI", 10, "bold"), padding=(14, 10), borderwidth=0)
		style.map("Secondary.TButton", background=[("active", "#d6e2e5")])
		style.configure("TNotebook", background="#eef3f7", borderwidth=0)
		style.configure("TNotebook.Tab", padding=(22, 10), font=("Segoe UI", 10, "bold"))
		style.configure("Input.TEntry", padding=10, font=("Segoe UI", 12))

	def build_ui(self):
		main = ttk.Frame(self.root, style="App.TFrame", padding=26)
		main.pack(fill=tk.BOTH, expand=True)

		header = ttk.Frame(main, style="Header.TFrame", padding=(26, 22))
		header.pack(fill=tk.X)
		ttk.Label(header, text="Calcwise", style="Title.TLabel").pack(anchor=tk.W)
		ttk.Label(header, text="Useful numbers, without the busywork.", style="Subtitle.TLabel").pack(
			anchor=tk.W, pady=(4, 0)
		)

		notebook = ttk.Notebook(main)
		notebook.pack(fill=tk.BOTH, expand=True, pady=(18, 0))
		interest_tab = ttk.Frame(notebook, style="Card.TFrame", padding=28)
		age_tab = ttk.Frame(notebook, style="Card.TFrame", padding=28)
		notebook.add(interest_tab, text="Simple Interest")
		notebook.add(age_tab, text="Age Calculator")
		self.build_interest_tab(interest_tab)
		self.build_age_tab(age_tab)

	def build_interest_tab(self, tab):
		content = ttk.Frame(tab, style="Card.TFrame")
		content.pack(fill=tk.BOTH, expand=True)
		content.columnconfigure(0, weight=3)
		content.columnconfigure(1, weight=2)
		left = ttk.Frame(content, style="Card.TFrame")
		left.grid(row=0, column=0, sticky="nsew", padx=(0, 24))
		ttk.Label(left, text="Calculate simple interest", style="Label.TLabel").pack(anchor=tk.W)
		ttk.Label(left, text="Interest = Principal x Rate x Time / 100", style="Muted.TLabel").pack(
			anchor=tk.W, pady=(5, 22)
		)
		form = ttk.Frame(left, style="Card.TFrame")
		form.pack(fill=tk.X)
		self.principal_entry = self.add_field(form, "Principal (Rs.)", self.principal_var, 0)
		self.rate_entry = self.add_field(form, "Annual rate (%)", self.rate_var, 1)
		self.time_entry = self.add_field(form, "Time (years)", self.time_var, 2)
		buttons = ttk.Frame(left, style="Card.TFrame")
		buttons.pack(fill=tk.X, pady=(24, 26))
		ttk.Button(buttons, text="Calculate interest", command=self.calculate_interest,
				   style="Accent.TButton").pack(side=tk.LEFT, fill=tk.X, expand=True)
		ttk.Button(buttons, text="Reset", command=self.reset_interest,
				   style="Secondary.TButton").pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
		self.make_result_panel(content, "SIMPLE INTEREST", self.interest_result_var,
							   self.interest_status_var, 1)
		self.principal_entry.focus_set()

	def build_age_tab(self, tab):
		current_year = date.today().year
		content = ttk.Frame(tab, style="Card.TFrame")
		content.pack(fill=tk.BOTH, expand=True)
		content.columnconfigure(0, weight=3)
		content.columnconfigure(1, weight=2)
		left = ttk.Frame(content, style="Card.TFrame")
		left.grid(row=0, column=0, sticky="nsew", padx=(0, 24))
		ttk.Label(left, text="Find your age", style="Label.TLabel").pack(anchor=tk.W)
		ttk.Label(left, text=f"Your age is calculated for the year {current_year}.",
				  style="Muted.TLabel").pack(anchor=tk.W, pady=(5, 22))
		form = ttk.Frame(left, style="Card.TFrame")
		form.pack(fill=tk.X)
		self.birth_year_entry = self.add_field(form, "Birth year", self.birth_year_var, 0)
		buttons = ttk.Frame(left, style="Card.TFrame")
		buttons.pack(fill=tk.X, pady=(24, 26))
		ttk.Button(buttons, text="Calculate age", command=self.calculate_age,
				   style="Accent.TButton").pack(side=tk.LEFT, fill=tk.X, expand=True)
		ttk.Button(buttons, text="Reset", command=self.reset_age,
				   style="Secondary.TButton").pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(10, 0))
		self.make_result_panel(content, "YOUR AGE", self.age_result_var, self.age_status_var, 1)

	def add_field(self, parent, label, variable, row):
		padding = (0, 8 if row == 0 else 16)
		ttk.Label(parent, text=label, style="Label.TLabel").grid(
			row=row, column=0, sticky=tk.W, pady=padding
		)
		entry = ttk.Entry(parent, textvariable=variable, style="Input.TEntry")
		entry.grid(row=row, column=1, sticky=tk.EW, padx=(20, 0), pady=padding)
		parent.columnconfigure(1, weight=1)
		return entry

	def make_result_panel(self, parent, heading, value_var, status_var, column):
		panel = tk.Frame(parent, bg="#f2f7f6", padx=22, pady=24)
		panel.grid(row=0, column=column, sticky="nsew")
		ttk.Label(panel, text=heading, style="ResultPanel.TLabel").pack(anchor=tk.W)
		ttk.Label(panel, textvariable=value_var, style="Result.TLabel").pack(anchor=tk.W, pady=(12, 8))
		ttk.Label(panel, textvariable=status_var, style="ResultPanel.TLabel", wraplength=180).pack(anchor=tk.W)

	def calculate_interest(self):
		try:
			principal = self.read_positive_number(self.principal_var.get(), "Principal")
			rate = self.read_positive_number(self.rate_var.get(), "Rate")
			time = self.read_positive_number(self.time_var.get(), "Time")
		except ValueError as error:
			messagebox.showerror("Invalid input", str(error))
			return
		interest = principal * rate * time / 100
		self.interest_result_var.set(f"Rs. {interest:,.2f}")
		self.interest_status_var.set(f"Rs. {principal:,.2f} at {rate:g}% for {time:g} years")

	def calculate_age(self):
		try:
			birth_year = int(self.birth_year_var.get().strip())
		except ValueError:
			messagebox.showerror("Invalid year", "Enter a whole-number birth year.")
			return
		current_year = date.today().year
		if birth_year < 1 or birth_year > current_year:
			messagebox.showerror("Invalid year", f"Enter a year from 1 to {current_year}.")
			return
		age = current_year - birth_year
		self.age_result_var.set(f"{age} years")
		self.age_status_var.set(f"Based on your birth year of {birth_year}")

	@staticmethod
	def read_positive_number(raw_value, field_name):
		try:
			value = float(raw_value.strip())
		except ValueError:
			raise ValueError(f"{field_name} must be a valid number.")
		if value < 0:
			raise ValueError(f"{field_name} cannot be negative.")
		return value

	def reset_interest(self):
		self.principal_var.set("")
		self.rate_var.set("")
		self.time_var.set("")
		self.interest_result_var.set("Rs. 0.00")
		self.interest_status_var.set("Enter the values to calculate interest")
		self.principal_entry.focus_set()

	def reset_age(self):
		self.birth_year_var.set("")
		self.age_result_var.set("0 years")
		self.age_status_var.set("Enter your birth year")
		self.birth_year_entry.focus_set()


def main():
	root = tk.Tk()
	CalculatorApp(root)
	root.mainloop()


if __name__ == "__main__":
	main()