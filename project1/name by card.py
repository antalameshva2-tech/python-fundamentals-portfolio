import tkinter as tk
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageTk
    HAS_PIL = True
except ImportError:
    HAS_PIL = False


class MyNameCardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Name Card")
        self.root.geometry("1200x760")
        self.root.configure(bg="#edf2f7")
        self.root.resizable(False, False)

        self.photo_path = Path(__file__).with_name("meshva.png")
        self.fields = {}
        self.build_form_screen()

    def build_form_screen(self):
        self.form_frame = tk.Frame(self.root, bg="#edf2f7")
        self.form_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        title = tk.Label(
            self.form_frame,
            text="Create Your Profile Card",
            font=("Segoe UI", 28, "bold"),
            bg="#edf2f7",
            fg="#1d2a48",
        )
        title.pack(anchor=tk.W, pady=(0, 20))

        form_box = tk.Frame(self.form_frame, bg="#ffffff", padx=30, pady=25)
        form_box.pack(fill=tk.BOTH, expand=True)

        labels = [
            ("Full Name", "name"),
            ("Age", "age"),
            ("City", "city"),
            ("Hobby", "hobby"),
            ("Programming Language", "language"),
            ("Role / Title", "role"),
        ]

        for label_text, key in labels:
            row = tk.Frame(form_box, bg="#ffffff")
            row.pack(fill=tk.X, pady=10)

            lbl = tk.Label(
                row,
                text=label_text,
                font=("Segoe UI", 12, "bold"),
                bg="#ffffff",
                fg="#1d2a48",
                width=18,
                anchor=tk.W,
            )
            lbl.pack(side=tk.LEFT)

            entry = tk.Entry(
                row,
                font=("Segoe UI", 12),
                width=40,
                bg="#f2f5f9",
                fg="#1d2a48",
                borderwidth=1,
                relief=tk.FLAT,
            )
            entry.pack(side=tk.LEFT, padx=(20, 0), ipady=7)
            self.fields[key] = entry

        submit_btn = tk.Button(
            form_box,
            text="Submit",
            bg="#0d7ef7",
            fg="white",
            font=("Segoe UI", 14, "bold"),
            padx=30,
            pady=12,
            borderwidth=0,
            relief=tk.FLAT,
            cursor="hand2",
            command=self.submit_form,
        )
        submit_btn.pack(pady=(20, 0))

    def submit_form(self):
        values = {}
        for key, entry in self.fields.items():
            value = entry.get().strip()
            if not value:
                tk.messagebox.showerror("Missing Data", f"Please fill {key}.")
                return
            values[key] = value

        self.profile_name = values["name"]
        self.profile_age = values["age"]
        self.profile_city = values["city"]
        self.profile_hobby = values["hobby"]
        self.profile_language = values["language"]
        self.profile_role = values["role"]

        self.form_frame.destroy()
        self.show_profile_card()

    def show_profile_card(self):
        outer = tk.Frame(self.root, bg="#0f8efb", padx=10, pady=10)
        outer.pack(fill=tk.BOTH, expand=True)

        card = tk.Frame(outer, bg="#eaf0f5", padx=28, pady=18, highlightthickness=0)
        card.pack(fill=tk.BOTH, expand=True)

        top_strip = tk.Frame(card, bg="#0d7ef7", height=18)
        top_strip.pack(fill=tk.X)

        inner = tk.Frame(card, bg="#edf2f7", padx=24, pady=18)
        inner.pack(fill=tk.BOTH, expand=True)

        left = tk.Frame(inner, bg="#edf2f7")
        left.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 22))

        photo_label = self.load_photo()
        if photo_label is not None:
            photo_label.pack(padx=10, pady=10)

        name_label = tk.Label(
            left,
            text=self.profile_name,
            font=("Segoe UI", 38, "bold"),
            bg="#edf2f7",
            fg="#1d2a48"
        )
        name_label.pack(pady=(12, 8))

        underline = tk.Frame(left, bg="#4d7df8", height=3, width=250)
        underline.pack(anchor=tk.CENTER)

        role = tk.Label(
            left,
            text=self.profile_role,
            bg="#7e6de9",
            fg="white",
            font=("Segoe UI", 18, "bold"),
            padx=18,
            pady=10,
            justify=tk.CENTER,
            width=22,
            anchor=tk.CENTER,
        )
        role.pack(pady=(18, 0))

        right = tk.Frame(inner, bg="#edf2f7")
        right.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        details = [
            ("Name", self.profile_name, "#3aa7ff"),
            ("Age", self.profile_age, "#2ec38d"),
            ("City", self.profile_city, "#b76ae6"),
            ("Hobby", self.profile_hobby, "#f5a623"),
            ("Programming\nLanguage", self.profile_language, "#f7507d"),
        ]

        for label_text, value, color in details:
            row = tk.Frame(right, bg="#f6f8fb", padx=18, pady=18, height=66)
            row.pack(fill=tk.X, pady=8, ipady=5)

            icon = tk.Label(
                row,
                text=self.icon_for(label_text),
                font=("Segoe UI", 20, "bold"),
                bg=color,
                fg="white",
                width=2,
                height=1,
                padx=10,
                pady=8,
            )
            icon.pack(side=tk.LEFT, padx=(0, 18))

            label = tk.Label(
                row,
                text=label_text,
                font=("Segoe UI", 18, "bold"),
                bg="#f6f8fb",
                fg="#1d2a48",
            )
            label.pack(side=tk.LEFT, padx=(0, 20), pady=8)

            colon = tk.Label(row, text=":", font=("Segoe UI", 18, "bold"), bg="#f6f8fb", fg="#1d2a48")
            colon.pack(side=tk.LEFT, pady=8)

            val = tk.Label(
                row,
                text=value,
                font=("Segoe UI", 20, "bold"),
                bg="#f6f8fb",
                fg="#1d2a48",
            )
            val.pack(side=tk.LEFT, padx=(10, 0), pady=8)

        footer = tk.Frame(card, bg="#7e6de9", height=70)
        footer.pack(fill=tk.X, pady=(16, 0))

        quote_left = tk.Label(footer, text='“', font=("Segoe UI", 28, "bold"), bg="#7e6de9", fg="white")
        quote_left.pack(side=tk.LEFT, padx=(20, 8), pady=10)

        quote = tk.Label(
            footer,
            text="Keep Learning, Keep Growing!",
            font=("Segoe UI", 20, "bold"),
            bg="#7e6de9",
            fg="white",
        )
        quote.pack(side=tk.LEFT, padx=10, pady=10)

        quote_right = tk.Label(footer, text='”', font=("Segoe UI", 28, "bold"), bg="#7e6de9", fg="white")
        quote_right.pack(side=tk.LEFT, padx=(8, 20), pady=10)

    def icon_for(self, label_text):
        mapping = {
            "Name": "👤",
            "Age": "🎂",
            "City": "📍",
            "Hobby": "📖",
            "Programming\nLanguage": "</>",
        }
        return mapping.get(label_text, "•")

    def load_photo(self):
        if not self.photo_path.exists():
            return None

        if HAS_PIL:
            try:
                image = Image.open(self.photo_path).convert("RGBA")
                image = image.resize((350, 350), Image.Resampling.LANCZOS)
                mask = Image.new("L", (350, 350), 0)
                draw = ImageDraw.Draw(mask)
                draw.ellipse((0, 0, 349, 349), fill=255)
                rounded = Image.new("RGBA", (350, 350), (0, 0, 0, 0))
                rounded.paste(image, (0, 0), mask=mask)
                tk_image = ImageTk.PhotoImage(rounded)
                photo = tk.Label(self.root, image=tk_image, bg="#edf2f7")
                photo.image = tk_image
                return photo
            except Exception:
                return None
        else:
            try:
                tk_image = tk.PhotoImage(file=str(self.photo_path))
                photo = tk.Label(self.root, image=tk_image, bg="#edf2f7")
                photo.image = tk_image
                return photo
            except Exception:
                return None


def main():
    root = tk.Tk()
    app = MyNameCardApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
