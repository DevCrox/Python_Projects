"""
Password Generator Application
----------------------------
A modern GUI application for generating secure passwords with customizable options.
Built using CustomTkinter for a modern look and feel.

Author: [Your Name]
Version: 1.0
"""

import customtkinter
import string
import random
from pyperclip import copy
from tkinter import PhotoImage, Menu
import sys
import os


def resource_path(relative_path):
    """
    Get absolute path to resource, works for both development and PyInstaller.
    
    Args:
        relative_path (str): Relative path to the resource file
        
    Returns:
        str: Absolute path to the resource
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def generate_password(length, use_numbers=True, use_symbols=True, use_uppercase=True):
    """
    Generate a secure random password based on specified criteria.
    
    Args:
        length (int): Length of the password
        use_numbers (bool): Include numbers in password
        use_symbols (bool): Include special symbols in password
        use_uppercase (bool): Include uppercase letters in password
        
    Returns:
        str: Generated password
    """
    characters = string.ascii_lowercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase
    global passkey
    passkey = ''.join(random.choice(characters) for _ in range(length))

    return passkey

def GUI():
    """
    Create and run the main GUI window for the password generator.
    Handles all UI elements and their interactions.
    """
    # Making the window
    appearance = customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")

    window = customtkinter.CTk()
    window_height = 350
    window_width = 525
    window.title("Password Generator")

    # Center the window on screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))
    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    # Main Frame setup
    main_frame = customtkinter.CTkFrame(master=window, fg_color="#161616")
    main_frame.pack(pady=0, padx=0, fill="both", expand=True)

    # Content Frame
    frame = customtkinter.CTkFrame(master = main_frame)
    frame.pack(pady=20, padx=60, fill="both", expand=True)

    # Canvas configuration
    canvas = customtkinter.CTkCanvas(master=main_frame, width=175, height=350, bg = "black", highlightthickness=0)
    canvas.place(x=1000, y=0)
    canvas.lift(True)

    # Grid configuration
    frame.columnconfigure((0,1,2), weight = 3)
    frame.rowconfigure((0,1,2,3,4,5,6), weight = 1)

    # Parameters Frame
    pframe = customtkinter.CTkFrame(master= frame)
    pframe.grid(column=0, row=4, columnspan= 3,rowspan= 1,sticky = "news")

    frame.columnconfigure((0,1,2), weight = 3)
    frame.rowconfigure((0,1), weight = 1)

    # Load UI assets
    copimage = PhotoImage(file=resource_path("Assets\\Copy.png"))
    retry = PhotoImage(file=resource_path("Assets\\Regenerate.png"))

    # UI Elements
    lbl2 = customtkinter.CTkLabel(master=pframe, text="  Password length : ", font = ("Arial Bold", 13)).grid(column= 0, row= 0)

    # Password length dropdown
    entry1_var = customtkinter.StringVar(value="16")
    entry1 = customtkinter.CTkOptionMenu(master=pframe,dropdown_fg_color="#041819",values=["8","10","12","13","14","15","16","32"], variable=entry1_var).grid(column = 1, row = 0, columnspan= 3, pady=10)

    # Password complexity options
    uppercase_var = customtkinter.BooleanVar(value=True)
    uppercase = customtkinter.CTkCheckBox(master=pframe, text="Uppercase", variable=uppercase_var).grid(column = 0, row = 1)

    numbers_var = customtkinter.BooleanVar(value=True)
    numbers = customtkinter.CTkCheckBox(master=pframe, text="Numbers", variable=numbers_var).grid(column = 2, row = 1, pady=10)

    symbols_var = customtkinter.BooleanVar(value=True)
    symbols = customtkinter.CTkCheckBox(master=pframe, text="Symbols", variable=symbols_var).grid(column = 5, row = 1)

    show_password = customtkinter.StringVar()

    def generate():
        """Generate a new password based on current settings."""
        length = int(entry1_var.get())
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        use_uppercase = uppercase_var.get()
        
        passkey = generate_password(length, use_numbers, use_symbols, use_uppercase)
        show_password.set(passkey)
        return passkey

    def copyc():
        """Copy the current password to clipboard."""
        copy(passkey)
    
    # Password display and control buttons
    show_password = customtkinter.StringVar(value = generate())
    if customtkinter.get_appearance_mode() == "Light" :
        password = customtkinter.CTkLabel(master=frame, textvariable=show_password, font=("Roboto",20), fg_color= "#3394CB").grid(column = 0, row = 0, columnspan= 3, padx=15, sticky = "ew")
        retrybutton = customtkinter.CTkButton(master=frame, text="Regenerate", image= retry, fg_color="#0F6495", command=generate).grid(column = 2, row=2)
        copybutton = customtkinter.CTkButton(master=frame, text="Copy", image= copimage, fg_color="#0F6495", command=copyc).grid(column = 0, row=2)
    else :
        password = customtkinter.CTkLabel(master=frame, textvariable=show_password, font=("Roboto",20), fg_color= "#252C2C").grid(column = 0, row = 0, columnspan= 3, padx=15, sticky = "ew")
        retrybutton = customtkinter.CTkButton(master=frame, text="Regenerate", image= retry, fg_color="#252C2C", command=generate).grid(column = 2, row=2)
        copybutton = customtkinter.CTkButton(master=frame, text="Copy", image= copimage, fg_color="#252C2C", command=copyc).grid(column = 0, row=2)

    window.mainloop()

if __name__ == "__main__":
    GUI()