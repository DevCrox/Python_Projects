import customtkinter
import string
import random
from pyperclip import copy
import sys
import os
from PIL import Image


def all() :
    def resource_path(relative_path):
        """ Get absolute path to resource, works for dev and for PyInstaller """
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS2
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    # Creating the password :
    def generate_password(length, use_numbers=True, use_symbols=True, use_uppercase=True):
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
    # Making the window
        appearance = customtkinter.set_appearance_mode("system")

        customtkinter.set_default_color_theme("dark-blue")

        win = customtkinter.CTk()
        #window.geometry("500x350")
        win_height = 350
        win_width = 500
        win.title("Password Generator")

        screen_width = win.winfo_screenwidth()
        screen_height = win.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (win_width/2))
        y_cordinate = int((screen_height/2) - (win_height/2))

        win.geometry("{}x{}+{}+{}".format(win_width, win_height, x_cordinate, y_cordinate))

    # Main Frame :
        main_frame = customtkinter.CTkFrame(master=win, fg_color="#161616")
        main_frame.pack(pady=0, padx=0, fill="both", expand=True)

    # Making the Frame
        frame = customtkinter.CTkFrame(master = main_frame)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

    # Config of the canvas :
        canvas = customtkinter.CTkCanvas(master=main_frame, width=175, height=350, bg = "black", highlightthickness=0)
        canvas.place(x=1000, y=0)
        canvas.lift(True)

    # Configure the Grid
        frame.columnconfigure((0,1,2), weight = 3)
        frame.rowconfigure((0,1,2,3,4,5,6), weight = 1)

    #Parameters Frame
        pframe = customtkinter.CTkFrame(master= frame)
        pframe.grid(column=0, row=4, columnspan= 3,rowspan= 1,sticky = "news")

    #Configure the grid
        frame.columnconfigure((0,1,2), weight = 3)
        frame.rowconfigure((0,1), weight = 1)


    # Interface Widgets :

        lbl2 = customtkinter.CTkLabel(master=pframe, text="  Password length : ", font = ("Arial Bold", 13)).grid(column= 0, row= 0)

        entry1_var = customtkinter.StringVar(value="16")
        entry1 = customtkinter.CTkOptionMenu(master=pframe,dropdown_fg_color="#041819",values=["8","10","12","13","14","15","16","32"], variable=entry1_var).grid(column = 1, row = 0, columnspan= 3, pady=10)

    #entry1.grid()
    # Password's settings checkboxes :
        uppercase_var = customtkinter.BooleanVar(value=True)
        uppercase = customtkinter.CTkCheckBox(master=pframe, text="Uppercase", variable=uppercase_var).grid(column = 0, row = 1)

        numbers_var = customtkinter.BooleanVar(value=True)
        numbers = customtkinter.CTkCheckBox(master=pframe, text="Numbers", variable=numbers_var).grid(column = 2, row = 1, pady=10)

        symbols_var = customtkinter.BooleanVar(value=True)
        symbols = customtkinter.CTkCheckBox(master=pframe, text="Symbols", variable=symbols_var).grid(column = 5, row = 1)

        show_password = customtkinter.StringVar()

    # generate function
        def generate():
            length = int(entry1_var.get())
            use_numbers = numbers_var.get()
            use_symbols = symbols_var.get()
            use_uppercase = uppercase_var.get()
            
            passkey = generate_password(length, use_numbers, use_symbols, use_uppercase)
            show_password.set(passkey)
            if customtkinter.get_appearance_mode() == "Light" :
                password = customtkinter.CTkLabel(master=frame, text= passkey, font=("Roboto",20), fg_color= "#3394CB" ).grid(column = 0, row = 0, columnspan= 3, padx=15, sticky = "ew")
            else :
                password = customtkinter.CTkLabel(master=frame, text=passkey, font=("Roboto",20), fg_color= "#252C2C").grid(column = 0, row = 0, columnspan= 3, padx=15, sticky = "ew")
            return passkey

    # Copy function :
        def copyc():
            copy(passkey)
        
        def back():
            win.destroy()
    # Creating The Password Label, +Both copy and retry buttons :
        show_password = customtkinter.StringVar()
        if customtkinter.get_appearance_mode() == "Light" :
            
            retrybutton = customtkinter.CTkButton(master=frame, text="(Re)generate", fg_color="#0F6495", command=generate).grid(column = 2, row=2)
            copybutton = customtkinter.CTkButton(master=frame, text="Copy", fg_color="#0F6495", command=copyc).grid(column = 0, row=2)

        else :
            
            retrybutton = customtkinter.CTkButton(master=frame, text="(Re)generate", fg_color="#252C2C", command=generate).grid(column = 2, row=2)
            copybutton = customtkinter.CTkButton(master=frame, text="Copy", fg_color="#252C2C", command=copyc).grid(column = 0, row=2)

    #Settings Button :
        back_but = customtkinter.CTkButton(master=main_frame, text="Back", width=0, command= back).place(x = 5, y = 5)
        win.bind('<Escape>', lambda event: back())

        win.mainloop()
    GUI()
    
