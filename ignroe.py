import tkinter as tk
from tkinter import messagebox

def show_popup():
    messagebox.showwarning("🚨 ALERT 🚨", 
        "You have won a FREE iPhone!\n\nClick OK to claim your prize now!")

root = tk.Tk()
root.withdraw()  

show_popup()
