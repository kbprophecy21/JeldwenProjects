import tkinter as tk
from tkinter import messagebox
from dataManager import DataManager

class BarcodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EFF Scanner GUI")
        self.data_manager = DataManager()

        self.label = tk.Label(root, text="Scan or Enter Barcode:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=5)
        self.entry.focus()

        self.submit_btn = tk.Button(root, text="Submit", command=self.submit_barcode)
        self.submit_btn.pack(pady=10)

        self.status = tk.Label(root, text="", fg="green")
        self.status.pack(pady=5)

    def submit_barcode(self):
        barcode = self.entry.get().strip()
        if not barcode:
            self.status.config(text="Please enter a barcode.", fg="red")
            return
        try:
            self.data_manager.update_from_barcode(barcode)
            self.status.config(text="Barcode accepted and data updated.", fg="green")
            self.entry.delete(0, tk.END)
        except Exception as e:
            self.status.config(text=f"Error: {e}", fg="red")

    def run_app():
        root = tk.Tk()
        app = BarcodeApp(root)
        root.mainloop()