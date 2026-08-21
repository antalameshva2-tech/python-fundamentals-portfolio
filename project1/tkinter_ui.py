import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import font as tkFont
import tkinter.scrolledtext as scrolledtext

class PersonalIntroductionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Introduction Card")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Set background color
        self.root.configure(bg="#f0f0f0")
        
        # Configure styles
        self.setup_styles()
        
        # Create main frame
        self.main_frame = ttk.Frame(root, style="Main.TFrame")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create header
        self.create_header()
        
        # Create form frame
        self.form_frame = ttk.Frame(self.main_frame, style="Form.TFrame")
        self.form_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Create form fields
        self.create_form_fields()
        
        # Create buttons
        self.create_buttons()
        
        # Store data
        self.data = {}
        
    def setup_styles(self):
        """Setup custom styles for the application"""
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure frame styles
        style.configure("Main.TFrame", background="#f0f0f0")
        style.configure("Form.TFrame", background="#ffffff", relief="raised", borderwidth=1)
        style.configure("Header.TLabel", background="#667eea", foreground="white", font=("Segoe UI", 18, "bold"))
        style.configure("Label.TLabel", background="#ffffff", font=("Segoe UI", 10, "bold"), foreground="#333333")
        style.configure("Text.TLabel", background="#ffffff", font=("Segoe UI", 10), foreground="#666666")
        
        # Configure button styles
        style.configure("Submit.TButton", font=("Segoe UI", 10, "bold"))
        style.map("Submit.TButton",
                  background=[('pressed', '#764ba2'), ('active', '#667eea')],
                  foreground=[('pressed', 'white'), ('active', 'white')])
        
        style.configure("Reset.TButton", font=("Segoe UI", 10))
        
    def create_header(self):
        """Create header section"""
        header_frame = tk.Frame(self.main_frame, bg="#667eea", height=80)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="📋 Personal Introduction", 
                              bg="#667eea", fg="white", font=("Segoe UI", 20, "bold"))
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame, text="Tell us about yourself", 
                                 bg="#667eea", fg="white", font=("Segoe UI", 12))
        subtitle_label.pack(pady=5)
        
    def create_form_fields(self):
        """Create form input fields"""
        # Name
        tk.Label(self.form_frame, text="Name", bg="#ffffff", font=("Segoe UI", 10, "bold"), 
                fg="#333333").grid(row=0, column=0, sticky=tk.W, pady=(10, 5))
        self.name_entry = ttk.Entry(self.form_frame, font=("Segoe UI", 10), width=30)
        self.name_entry.grid(row=0, column=1, sticky=tk.EW, pady=(10, 15))
        
        # Age
        tk.Label(self.form_frame, text="Age", bg="#ffffff", font=("Segoe UI", 10, "bold"), 
                fg="#333333").grid(row=1, column=0, sticky=tk.W, pady=(0, 5))
        self.age_entry = ttk.Entry(self.form_frame, font=("Segoe UI", 10), width=30)
        self.age_entry.grid(row=1, column=1, sticky=tk.EW, pady=(0, 15))
        
        # City
        tk.Label(self.form_frame, text="City", bg="#ffffff", font=("Segoe UI", 10, "bold"), 
                fg="#333333").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        self.city_entry = ttk.Entry(self.form_frame, font=("Segoe UI", 10), width=30)
        self.city_entry.grid(row=2, column=1, sticky=tk.EW, pady=(0, 15))
        
        # Hobby
        tk.Label(self.form_frame, text="Hobby", bg="#ffffff", font=("Segoe UI", 10, "bold"), 
                fg="#333333").grid(row=3, column=0, sticky=tk.W, pady=(0, 5))
        self.hobby_entry = ttk.Entry(self.form_frame, font=("Segoe UI", 10), width=30)
        self.hobby_entry.grid(row=3, column=1, sticky=tk.EW, pady=(0, 15))
        
        # Programming Language
        tk.Label(self.form_frame, text="Programming Language", bg="#ffffff", 
                font=("Segoe UI", 10, "bold"), fg="#333333").grid(row=4, column=0, sticky=tk.W, pady=(0, 5))
        
        self.language_var = tk.StringVar()
        language_options = ["Python", "JavaScript", "Java", "C++", "C#", "PHP", "Ruby", "Go", "Rust", "Other"]
        self.language_combo = ttk.Combobox(self.form_frame, textvariable=self.language_var, 
                                           values=language_options, font=("Segoe UI", 10), width=28, state="readonly")
        self.language_combo.grid(row=4, column=1, sticky=tk.EW, pady=(0, 15))
        
        # Configure grid weights
        self.form_frame.columnconfigure(1, weight=1)
        
    def create_buttons(self):
        """Create action buttons"""
        button_frame = ttk.Frame(self.form_frame, style="Form.TFrame")
        button_frame.grid(row=5, column=0, columnspan=2, sticky=tk.EW, pady=20)
        
        submit_btn = ttk.Button(button_frame, text="✓ Submit", command=self.submit_form, style="Submit.TButton")
        submit_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        reset_btn = ttk.Button(button_frame, text="↻ Clear", command=self.clear_form, style="Reset.TButton")
        reset_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
    def submit_form(self):
        """Handle form submission"""
        # Validate inputs
        name = self.name_entry.get().strip()
        age = self.age_entry.get().strip()
        city = self.city_entry.get().strip()
        hobby = self.hobby_entry.get().strip()
        language = self.language_var.get()
        
        if not all([name, age, city, hobby, language]):
            messagebox.showwarning("Validation Error", "Please fill in all fields!")
            return
        
        # Validate age
        try:
            age_int = int(age)
            if age_int < 1 or age_int > 120:
                messagebox.showwarning("Validation Error", "Age must be between 1 and 120!")
                return
        except ValueError:
            messagebox.showwarning("Validation Error", "Age must be a valid number!")
            return
        
        # Store data
        self.data = {
            "name": name,
            "age": age,
            "city": city,
            "hobby": hobby,
            "language": language
        }
        
        # Show results
        self.show_results()
        
    def clear_form(self):
        """Clear all form fields"""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.hobby_entry.delete(0, tk.END)
        self.language_combo.set("")
        
    def show_results(self):
        """Create and show results window"""
        results_window = tk.Toplevel(self.root)
        results_window.title("Your Introduction Card")
        results_window.geometry("500x500")
        results_window.resizable(False, False)
        
        # Header
        header_frame = tk.Frame(results_window, bg="#667eea", height=60)
        header_frame.pack(fill=tk.X)
        
        title_label = tk.Label(header_frame, text="📋 Your Personal Introduction", 
                              bg="#667eea", fg="white", font=("Segoe UI", 16, "bold"))
        title_label.pack(pady=15)
        
        # Results frame
        results_frame = tk.Frame(results_window, bg="#f9f9f9")
        results_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Display results
        result_items = [
            ("Name", self.data["name"]),
            ("Age", self.data["age"]),
            ("City", self.data["city"]),
            ("Hobby", self.data["hobby"]),
            ("Programming Language", self.data["language"])
        ]
        
        for i, (label, value) in enumerate(result_items):
            # Label
            label_widget = tk.Label(results_frame, text=label, bg="#f9f9f9", 
                                   font=("Segoe UI", 10, "bold"), fg="#667eea")
            label_widget.grid(row=i, column=0, sticky=tk.W, pady=(15, 5))
            
            # Value box
            value_frame = tk.Frame(results_frame, bg="white", bd=1, relief=tk.SOLID)
            value_frame.grid(row=i, column=0, columnspan=2, sticky=tk.EW, pady=(5, 0))
            
            value_widget = tk.Label(value_frame, text=value, bg="white", 
                                   font=("Segoe UI", 11), fg="#333333", justify=tk.LEFT)
            value_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        results_frame.columnconfigure(0, weight=1)
        
        # Action buttons
        button_frame = tk.Frame(results_window, bg="white")
        button_frame.pack(fill=tk.X, padx=20, pady=20)
        
        edit_btn = tk.Button(button_frame, text="✏️  Edit", command=results_window.destroy, 
                            bg="#667eea", fg="white", font=("Segoe UI", 10, "bold"), 
                            padx=20, pady=8, cursor="hand2", relief=tk.FLAT)
        edit_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
        print_btn = tk.Button(button_frame, text="🖨️  Print", command=lambda: self.print_results(results_window), 
                             bg="#e0e0e0", fg="#333333", font=("Segoe UI", 10, "bold"), 
                             padx=20, pady=8, cursor="hand2", relief=tk.FLAT)
        print_btn.pack(side=tk.LEFT, padx=5, fill=tk.X, expand=True)
        
    def print_results(self, window):
        """Print results (simulated)"""
        output = f"""
=====================================
        PERSONAL INTRODUCTION
=====================================

Name       : {self.data['name']}
Age        : {self.data['age']}
City       : {self.data['city']}
Hobby      : {self.data['hobby']}
Language   : {self.data['language']}

=====================================
        """
        
        # Create a print preview window
        print_window = tk.Toplevel(window)
        print_window.title("Print Preview")
        print_window.geometry("500x400")
        
        text_widget = scrolledtext.ScrolledText(print_window, font=("Courier", 11), 
                                               bg="white", fg="#333333")
        text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        text_widget.insert(1.0, output)
        text_widget.config(state=tk.DISABLED)
        
        messagebox.showinfo("Print", "Print preview opened!\n\nYou can use Ctrl+P in the preview window to print.")


def main():
    root = tk.Tk()
    app = PersonalIntroductionApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
