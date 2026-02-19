import tkinter as tk
import random
import string

def generate_password():
    length = 14
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

window = tk.Tk()
window.title("Генератор паролей")
window.geometry("300x100")

password_entry = tk.Entry(window, width=30, font=("Arial", 10))
password_entry.pack(pady=10)

generate_button = tk.Button(window, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(pady=5)

window.mainloop()
