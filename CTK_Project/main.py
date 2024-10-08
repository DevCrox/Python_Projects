import customtkinter
from time import time, sleep
from PIL import Image
import threading
import tkinter
import CustomPassGenerator
from datetime import datetime



def GUI():
# Useful things :
    sessions = dict()
    resting = dict()
# Making the window
    appearance = customtkinter.set_appearance_mode("system")
    customtkinter.set_default_color_theme("dark-blue")
    window = customtkinter.CTk()

# Getting screen size information :
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

#window.geometry("500x350")
    window_height = screen_height-58
    window_width = screen_width
    window.title("Work Planner & Manager")

    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    x_cordinate = -10
    y_cordinate = 0

    window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

    def make_frame():
        global frame
        global main_frame
        # Main Frame :
        main_frame = customtkinter.CTkFrame(master=window, fg_color="#161616")
        main_frame.pack(pady=0, padx=0, fill="both", expand=True)

        # Making the Frame
        frame = customtkinter.CTkFrame(master = main_frame)
        frame.pack(pady=20, padx=60, fill="both", expand=True)

        # Configure the Grid
        frame.columnconfigure((0,1,2), weight = 3)
        frame.rowconfigure((0,1,2,3,4,5,6), weight = 1)

# Importing .png files :
    pomodoro_img = customtkinter.CTkImage(light_image=Image.open("Assets\\pomodoro.png"),
                                          dark_image=Image.open("Assets\\pomodoro.png"),
                                          size= (300,150))
    timetable_img = customtkinter.CTkImage(light_image=Image.open("Assets\\timetable.png"),
                                          dark_image=Image.open("Assets\\timetable.png"),
                                          size= (220,150))
    study_sessions_img = customtkinter.CTkImage(light_image=Image.open("Assets\\study_sessions.png"),
                                                dark_image=Image.open("Assets\\study_sessions.png"),
                                                size= (300,150))  
    apple_img = customtkinter.CTkImage(light_image=Image.open("Assets\\apple.png"),
                                        dark_image=Image.open("Assets\\apple.png"),
                                        size= (500,500))
    passwordgen_img = customtkinter.CTkImage(light_image=Image.open("Assets\\SolXPass.png"),
                                        dark_image=Image.open("Assets\\SolXPass.png"),
                                        size= (300,150))
    exit_img = customtkinter.CTkImage(light_image=Image.open("Assets\\exit.png"),
                                        dark_image=Image.open("Assets\\exit.png"),
                                        size= (170,150))
    break_img = customtkinter.CTkImage(light_image=Image.open("Assets\\break.png"),
                                        dark_image=Image.open("Assets\\break.png"),
                                        size= (170,150))
    clock_img = customtkinter.CTkImage(light_image=Image.open("Assets\\clock.png"),
                                        dark_image=Image.open("Assets\\clock.png"),
                                        size= (50,50))


# Pomodoro Timer :
    def explain() :
        explain_lbl1 = customtkinter.CTkLabel(master= frame, text= "Pomodoro Method Explanation:", font=("Arial Bold", 20, "bold")).grid(column = 2, row = 1, sticky= "s")
        explain_lbl2 = customtkinter.CTkLabel(master= frame, text= "- Work 25 min", font=("Arial Bold", 20, "bold")).grid(column = 2, row = 2, sticky = "s")
        explain_lbl3 = customtkinter.CTkLabel(master= frame, text= "- Rest 5 min", font=("Arial Bold", 20, "bold")).grid(column = 2, row = 3, sticky = "n")

    def start_timer():
        global is_work_session
        global current_session
        is_work_session = True
        current_session = 0

        topass = 0
        rest_time = 0
        for widget in window.winfo_children():
            widget.destroy()
        make_frame()

        encourage_lazy_people = customtkinter.CTkButton(master= frame, text="Don't be lazy you'll soon notice progress !", font=("Arial Bold", 40, "bold"), command = explain)
        encourage_lazy_people.grid(column=0, row=0, sticky="n", columnspan = 3)

        back_but = customtkinter.CTkButton(master= frame, text="Back", command=back, font=("Arial Bold", 50, "bold"))
        back_but.grid(column=0, row=0, sticky="nw")
        window.bind('<Escape>', lambda event: back())
        
        apple = customtkinter.CTkLabel(master= frame, text= "", image= apple_img, width=500, height=500)
        apple.grid(column= 0, row= 0, columnspan= 3, rowspan=6)
        

        # Create a label to display the countdown
        countdown_label = customtkinter.CTkLabel(frame, text="", font=("Helvetica", 48))
        countdown_label.grid(column= 0, row= 3, columnspan=3)

        # State variables


        # Pomodoro settings
        work_duration = 25 * 60  # 25 minutes
        short_break_duration = 5 * 60  # 5 minutes
        long_break_duration = 15 * 60  # 15 minutes
        sessions_before_long_break = 4
        def next_time():
            global is_work_session
            global current_session
            switch_session(is_work_session, current_session)

        def start_pomodoro(is_work_session, current_session):
            if is_work_session:
                update_countdown(work_duration)
            else:
                if current_session % sessions_before_long_break == 0:
                    update_countdown(long_break_duration)
                else:
                    update_countdown(short_break_duration)

        def update_countdown(total_seconds):
            if total_seconds >= 0:
                # Calculate minutes and seconds
                mins, secs = divmod(total_seconds, 60)
                time_format = f"{mins:02d}:{secs:02d}"
                
                # Update the label text
                countdown_label.configure(text=time_format)
                
                # Call this function again after 1 second
                window.after(1000, update_countdown, total_seconds - 1)
            else:
                next_time()
                
        
        def switch_session(is_work_session, current_session):
            if is_work_session:
                current_session += 1
                is_work_session = not is_work_session
            
            start_pomodoro(is_work_session, current_session)
        start_pomodoro(is_work_session, current_session)
# Go back to the main screen :
    def back():
        for widget in window.winfo_children():
            widget.destroy()
        next_page()

        # Create new widgets
# Pomodoro command
    def pomodoro_command():
        start_timer()

    def pass_app():
        CustomPassGenerator.all()
# Planning sessions
    def plan_session() :
        for widget in window.winfo_children():
            widget.destroy()
        make_frame()
        user_lbl1 = customtkinter.CTkLabel(master = frame, text="Session Planner", font=("Algerian", 80, "bold","underline"))
        user_lbl1.grid(column = 0, row = 0, columnspan = 3)

        back_but = customtkinter.CTkButton(master= frame, text="Back", command=back, font=("Arial Bold", 35, "bold"))
        back_but.grid(column=0, row=0, sticky="nw")
        window.bind('<Escape>', lambda event: back())

        option_lbl = customtkinter.CTkLabel(master = frame, text="Options", font=("Algerian", 40, "bold"))
        option_lbl.grid(column = 2, row = 1)

        entry1_var = customtkinter.StringVar(value="Choose an Option..")
        entry1 = customtkinter.CTkOptionMenu(master=frame,dropdown_fg_color="#0E6C7D", dynamic_resizing=True, dropdown_font=("Arial Bold", 18, "bold"), width=250, height= 50,values=["Arabic","French","English","SVT","PC","E.I","Maths","Rest..","Other.."], variable=entry1_var)
        entry1.grid(column = 2, row = 2, sticky = "n")

        slider = customtkinter.CTkSlider(master= frame, from_=0, to=23, number_of_steps=24, orientation="horizontal", width= 1200)
        slider.grid(column = 0, row = 3, columnspan= 3, sticky="s")

        # Special frame for the label hour
        label_frame = customtkinter.CTkFrame(master= frame)
        label_frame.grid(column = 0, row = 4, columnspan= 3, sticky = "ew")

        for hour in range(24):
            label = customtkinter.CTkLabel(master=label_frame, text=f"{hour:02d}:00", font= ("Arial Bold", 17, "bold"))
            label.grid(row=4, column=hour, padx=5, sticky = "new")
        
        # Adding notes
        user_lbl2 = customtkinter.CTkLabel(master = frame, text="Notes : ", font=("Algerian", 40, "bold"))
        user_lbl2.grid(column = 0, row = 1, sticky = "ew")

        notes = customtkinter.CTkEntry(master = frame, width= 400, height= 300)
        notes.grid(column = 0, row = 2)

        def enter():
            saved = customtkinter.CTkLabel(master = frame, text="Saved ! ", font=("Algerian",20, "bold"))
            saved.grid(column = 2, row = 0, sticky = "ne")

            # Get the selected option and hour from the GUI
            selected_option = entry1_var.get()
            hour = slider.get()
            note = notes.get()
            print(f"Option: {selected_option}, Hour: {int(hour)}, Note: {note}")
            if selected_option != "Rest.." :
                sessions[selected_option] = str(int(hour)) + "h -" + note
            else :
                resting[selected_option] = str(int(hour)) + "h -" + note

            print(sessions)


        enter_button = customtkinter.CTkButton(master = frame,text = "Enter" ,command=enter)
        enter_button.grid(column = 0, row = 5, columnspan= 3)
        window.bind('<Return>', lambda event: enter())
# Visualize session
    def visualize():
        for widget in window.winfo_children():
            widget.destroy()
        make_frame()
        # Create new widgets
        sessions_label = customtkinter.CTkLabel(master = frame, text= "Study Sessions", font=("Algerian", 80, "bold","underline"))
        sessions_label.grid(column = 0, row = 0, columnspan=3)

        back_but = customtkinter.CTkButton(master= frame, text="Back", command=back, font=("Arial Bold", 35, "bold"))
        back_but.grid(column=0, row=0, sticky="nw")
        window.bind('<Escape>', lambda event: back())
        # Name of the frames :
        hour_title = customtkinter.CTkLabel(master = frame, text= "Hour", font=("Algerian", 40, "bold","underline"))
        hour_title.grid(column = 0, row = 1, sticky="sew")

        options_title = customtkinter.CTkLabel(master = frame, text= "Option", font=("Algerian", 40, "bold","underline"))
        options_title.grid(column = 1, row = 1, sticky="sew")

        note_title = customtkinter.CTkLabel(master = frame, text= "Note", font=("Algerian", 40, "bold","underline"))
        note_title.grid(column = 2, row = 1, sticky="sew")
        # Get the saved sessions from the GUI
        hours_frame = customtkinter.CTkFrame(master= frame)
        hours_frame.grid(column = 0, row = 2, rowspan=8, sticky="news", pady=10, padx=10)

        subjects_frame = customtkinter.CTkFrame(master= frame)
        subjects_frame.grid(column = 1, row = 2, rowspan=8, sticky="news", pady = 10, padx = 10)

        notes_frame = customtkinter.CTkFrame(master= frame)
        notes_frame.grid(column = 2, row = 2, rowspan=8, sticky="news", pady = 10, padx = 10)

        # Rest goes right to the rest dictionary :

        for i, (option, session) in enumerate(sessions.items()):
            

            hour, note = session.split("h -")
            hour_label = customtkinter.CTkLabel(master=hours_frame, text=f"{hour}", font=("Arial", 25))
            hour_label.grid(row=i, column=0, pady=2, padx=5, sticky="ew")

            subject_label = customtkinter.CTkLabel(master=subjects_frame, text=f"{option}", font=("Arial", 25))
            subject_label.grid(row=i, column=0, pady=2, padx=5, sticky="ew")

            note_label = customtkinter.CTkLabel(master=notes_frame, text=f"{note}", font=("Arial", 25))
            note_label.grid(row=i, column=0, pady=2, padx=5, sticky="ew")
#Visualize Rest Sessions
    def visualize_rest():
        for widget in window.winfo_children():
            widget.destroy()
        make_frame()
        # Create new widgets
        sessions_label = customtkinter.CTkLabel(master = frame, text= "Rest Sessions", font=("Algerian", 80, "bold","underline"))
        sessions_label.grid(column = 0, row = 0, columnspan=3)

        back_but = customtkinter.CTkButton(master= frame, text="Back", command=back, font=("Arial Bold", 35, "bold"))
        back_but.grid(column=0, row=0, sticky="nw")
        window.bind('<Escape>', lambda event: back())
        # Name of the frames :
        hour_title = customtkinter.CTkLabel(master = frame, text= "Hour", font=("Algerian", 40, "bold","underline"))
        hour_title.grid(column = 0, row = 1, sticky="sew")

        options_title = customtkinter.CTkLabel(master = frame, text= "Option", font=("Algerian", 40, "bold","underline"))
        options_title.grid(column = 1, row = 1, sticky="sew")

        note_title = customtkinter.CTkLabel(master = frame, text= "Note", font=("Algerian", 40, "bold","underline"))
        note_title.grid(column = 2, row = 1, sticky="sew")
        # Get the saved sessions from the GUI
        hours_frame = customtkinter.CTkFrame(master= frame)
        hours_frame.grid(column = 0, row = 2, rowspan=8, sticky="news", pady=10, padx=10)

        subjects_frame = customtkinter.CTkFrame(master= frame)
        subjects_frame.grid(column = 1, row = 2, rowspan=8, sticky="news", pady = 10, padx = 10)

        notes_frame = customtkinter.CTkFrame(master= frame)
        notes_frame.grid(column = 2, row = 2, rowspan=8, sticky="news", pady = 10, padx = 10)

        # Rest goes right to the rest dictionary :
        for i, (option, session) in enumerate(resting.items()):
            

            hour, note = session.split("h -")
            hour_label = customtkinter.CTkLabel(master=hours_frame, text=f"{hour}", font=("Arial", 25))
            hour_label.grid(row=i, column=0, pady=2, padx=5, sticky="ew")

            subject_label = customtkinter.CTkLabel(master=subjects_frame, text=f"{option}", font=("Arial", 25))
            subject_label.grid(row=i, column=0, pady=2, padx=5, sticky="ew")

            note_label = customtkinter.CTkLabel(master=notes_frame, text=f"{note}", font=("Arial", 25))
            note_label.grid(row=i, column=0, pady=2, padx=5, sticky="ew")
# Defining functions :
    def next_page():
        make_frame()
        # Create new widgets
        
        hi = customtkinter.CTkLabel(master = frame, text= "Hello "+str(username)+ " :", font = ("default", 20, "bold")).grid(column= 0, row= 0, sticky="nw", padx= 10)
        studymanager_lbl = customtkinter.CTkLabel(master = frame, text= "Study Manager", font= ("Cooper Black", 100, "bold", "underline"))
        studymanager_lbl.grid(column= 0, row= 0, columnspan=3)

        pomodoro = customtkinter.CTkButton(master = frame, text= "Pomodoro", image= pomodoro_img, compound="top", font= ("Cooper Black", 25, "bold"), command= pomodoro_command)
        pomodoro.grid(column = 1, row = 1, sticky = "new", padx = 5, pady = 5)

        timetable = customtkinter.CTkButton(master = frame, text= "Planner", image= timetable_img, compound="top", font= ("Cooper Black", 25, "bold"), command = plan_session)
        timetable.grid(column = 0, row = 1, sticky = "new", padx = 5, pady = 5)

        study_sessions = customtkinter.CTkButton(master = frame, text= "Study sessions", image= study_sessions_img, compound="top", font= ("Cooper Black", 25, "bold"), command = visualize)
        study_sessions.grid(column = 2, row = 1, sticky = "new", padx = 5, pady = 5)

        password_generator = customtkinter.CTkButton(master = frame, text= "Password Generator", image= passwordgen_img, compound="top", font= ("Cooper Black", 25, "bold"), command = pass_app)
        password_generator.grid(column = 0, row = 2, sticky = "new", padx = 5, pady = 5)

        rest_sessions = customtkinter.CTkButton(master = frame, text= "Rest sessions", image= break_img, compound="top", font= ("Cooper Black", 25, "bold"), command = visualize_rest)
        rest_sessions.grid(column = 1, row = 2, sticky = "new", padx = 5, pady = 5)

        def exit():
            window.destroy()
        exit_button = customtkinter.CTkButton(master = frame, text="Exit the app", image= exit_img, compound="top", font= ("Cooper Black", 25, "bold"), command = exit)
        exit_button.grid(column = 2, row = 2, sticky = "new", padx = 5, pady = 5)

        # Getting hour details
        now = datetime.now()
        current_hour = str(now.hour)
        current_minute = str(now.minute)

        acctual_hour = customtkinter.CTkLabel(master = frame, text=current_hour+":"+current_minute+ "    ", image=clock_img, compound= "right", font= ("Cooper Black", 20, "bold"))
        acctual_hour.grid(column = 2, row =0, sticky = "ne")
# Adding Widgets :
    make_frame()

    user_lbl1 = customtkinter.CTkLabel(master = frame, text="Welcome", font=("Algerian", 80, "bold","underline"))
    user_lbl1.grid(column = 0, row = 1, columnspan = 3)

    user_lbl2 = customtkinter.CTkLabel(master = frame, text="User : ", font=("Algerian", 40, "bold"))
    user_lbl2.grid(column = 0, row = 2, sticky = "e")
    
    username_entry = customtkinter.CTkEntry(master= frame)
    username_entry.grid(column = 1, row = 2, sticky = "ew")

    def get_user():
        global username
        username = username_entry.get()
        if len(username.replace(" ", "")) < 4 :
            showerror= customtkinter.CTkLabel(master= frame, text="Error: Username should be at least 4 characters long.(Spaces aren't allowed !)", bg_color= "red", font= ("Arial Bold", 20, "bold"))
            showerror.grid(column = 0, row = 4, columnspan= 3, sticky = "n")
        else :
            print(f"Hello, {username}!") # For debugging purposes
            for widget in window.winfo_children():
                widget.destroy()
            next_page()


    enter_but = customtkinter.CTkButton(master = frame, text="Enter",font= ("default", 25, "bold"), command= get_user, width=200, height= 40)
    enter_but.grid(column = 1 , row = 3, sticky = "n")
    window.bind('<Return>', lambda event: get_user())









    window.mainloop()
GUI()
