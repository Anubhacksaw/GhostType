import tkinter as tk
from tkinter import filedialog, messagebox
import pyautogui
import time
import random
import threading
import webbrowser

class TypingBot:
    def __init__(self, root):
        self.root = root
        self.text = ""
        self.typing_speed = 0.1
        self.start_delay = 10
        self.is_typing = False
        self.create_widgets()

    def create_widgets(self):
        self.root.geometry("500x600")
        self.root.config(bg='#2b2b2b')
        self.root.title("GostTyper V 1.0 BY @Anubhab Mukherjee")

        tk.Label(self.root, text="Enter or paste text below:", bg='#2b2b2b', fg='#ffffff', font=("Arial", 12)).pack(pady=10)
        self.text_box = tk.Text(self.root, height=10, width=50, bg='#1e1e1e', fg='#ffffff', insertbackground='#ffffff', relief='flat', wrap='word')
        self.text_box.pack(padx=10, pady=5)

        self.browse_button = tk.Button(self.root, text="Browse Text File", command=self.load_file, bg='#4CAF50', fg='#ffffff', font=("Arial", 10), relief='flat')
        self.browse_button.pack(pady=10)

        tk.Label(self.root, text="Start delay (seconds):", bg='#2b2b2b', fg='#ffffff', font=("Arial", 12)).pack(pady=5)
        self.delay_entry = tk.Entry(self.root, bg='#1e1e1e', fg='#ffffff', insertbackground='#ffffff', relief='flat')
        self.delay_entry.insert(0, "10")
        self.delay_entry.pack(pady=5)

        tk.Label(self.root, text="Typing speed (seconds per character):", bg='#2b2b2b', fg='#ffffff', font=("Arial", 12)).pack(pady=5)
        self.speed_entry = tk.Entry(self.root, bg='#1e1e1e', fg='#ffffff', insertbackground='#ffffff', relief='flat')
        self.speed_entry.insert(0, "0.1")
        self.speed_entry.pack(pady=5)

        button_frame = tk.Frame(self.root, bg='#2b2b2b')
        button_frame.pack(pady=20)

        self.start_button = tk.Button(button_frame, text="Start Typing", command=self.start_typing, bg='#4CAF50', fg='#ffffff', font=("Arial", 12), relief='flat', width=12)
        self.start_button.grid(row=0, column=0, padx=10)

        self.stop_button = tk.Button(button_frame, text="Stop Typing", command=self.stop_typing, state='disabled', bg='#f44336', fg='#ffffff', font=("Arial", 12), relief='flat', width=12)
        self.stop_button.grid(row=0, column=1, padx=10)

        self.contact_button = tk.Button(self.root, text="Contact", command=self.show_contact_info, bg='#007BFF', fg='#ffffff', font=("Arial", 10), relief='flat', width=12)
        self.contact_button.pack(pady=10)

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'r') as file:
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(tk.END, file.read())

    def start_typing(self):
        self.text = self.text_box.get("1.0", tk.END).strip()
        try:
            self.start_delay = int(self.delay_entry.get())
            self.typing_speed = float(self.speed_entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter valid numbers for delay and typing speed.")
            return

        if not self.text:
            messagebox.showerror("No text", "Please enter or load some text to type.")
            return

        self.delay_entry.config(state='disabled')
        self.speed_entry.config(state='disabled')
        self.start_button.config(state='disabled')
        self.stop_button.config(state='normal')

        messagebox.showinfo("Get Ready", f"Typing will start in {self.start_delay} seconds. Place your cursor!")
        self.is_typing = True
        threading.Thread(target=self.typing_logic).start()

    def stop_typing(self):
        if not self.is_typing:
            messagebox.showwarning("Warning", "Typing has not started yet.")
            return
        self.is_typing = False
        self.stop_button.config(state='disabled')
        self.delay_entry.config(state='normal')
        self.speed_entry.config(state='normal')
        self.start_button.config(state='normal')

    def typing_logic(self):
        time.sleep(self.start_delay)
        mistake_chance = 0.05
        speed2 = self.typing_speed / 2
        for char in self.text:
            if not self.is_typing:
                break
            if random.random() < mistake_chance:
                wchar = random.choice("abcdefghijklmnopqrstuvwxyz")
                pyautogui.write(wchar, interval=self.typing_speed + random.uniform(-speed2, speed2))
                time.sleep(0.3)
                pyautogui.press('backspace')
            typing_speed = self.typing_speed + random.uniform(-speed2, speed2)
            pyautogui.write(char, interval=typing_speed)
        self.is_typing = False
        self.stop_button.config(state='disabled')
        self.delay_entry.config(state='normal')
        self.speed_entry.config(state='normal')
        self.start_button.config(state='normal')

    def show_contact_info(self):
        contact_window = tk.Toplevel(self.root)
        contact_window.geometry("400x250")
        contact_window.config(bg='#2b2b2b')
        contact_window.title("Contact Information")

        tk.Label(contact_window, text="Name: Anubhab Mukherjee", bg='#2b2b2b', fg='#ffffff', font=("Arial", 12)).pack(pady=10)

        linkedin_label = tk.Label(contact_window, text="LinkedIn", bg='#2b2b2b', fg='#007BFF', font=("Arial", 10), cursor="hand2")
        linkedin_label.pack(pady=5)
        linkedin_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://in.linkedin.com/in/anubhab-mukherjee-019961204"))

        github_label = tk.Label(contact_window, text="GitHub", bg='#2b2b2b', fg='#007BFF', font=("Arial", 10), cursor="hand2")
        github_label.pack(pady=5)
        github_label.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/Anubhacksaw"))

        back_button = tk.Button(contact_window, text="Back", command=contact_window.destroy, bg='#007BFF', fg='#ffffff', font=("Arial", 10), relief='flat', width=12)
        back_button.pack(pady=10)

root = tk.Tk()
app = TypingBot(root)
root.mainloop()
