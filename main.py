import tkinter as tk
from tkinter import messagebox
from modules.qr_generator import QRGenerator
from modules.validation import LinkValidator
import sys
import os

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("QR Code Generator")
        self.root.geometry("400x300")
        self.root.resizable(False, False)  # Запрет изменения размеров окна
        self.save_path = "output"
        self.qr_generator = QRGenerator(self.save_path)
        self.create_widgets()
        
    def resource_path(relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath("."), relative_path)
    
    def create_widgets(self):
        tk.Label(self.root, text="Введите сслыку:").pack(pady=5)
        self.link_entry = tk.Entry(self.root, width=50)
        self.link_entry.pack(pady=5)

        tk.Label(self.root, text="Введите название итогового файла:").pack(pady=5)
        self.filename_entry = tk.Entry(self.root, width=50)
        self.filename_entry.pack(pady=5)

        self.generate_button = tk.Button(self.root, text="Создать QR Code", command=self.generate_qr_code)
        self.generate_button.pack(pady=20)

    def generate_qr_code(self):
        link = self.link_entry.get()
        filename = self.filename_entry.get()

        if not LinkValidator.validate(link):
            messagebox.showerror("Ошибка в ссылке")
            return

        if not filename.strip():
            messagebox.showerror("Ошибка в файле")
            return

        try:
            file_path = self.qr_generator.generate_qr(link, filename)
            messagebox.showinfo("Успешно", f"QR Code сохранен в: {file_path}")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
