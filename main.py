import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import add_user, get_user, delete_user

def signup():
    main_label.pack_forget()
    button_frame.pack_forget()

    signup_frame = tk.Frame()
    signup_frame.pack(anchor="center")

    signup_label = tk.Label(signup_frame, text="Signup", font=("Times New Roman", 24))
    signup_label.pack(pady=(100,75), anchor="center")

    username_label = tk.Label(signup_frame, text="Username:", font=("Times New Roman", 18))
    username_label.pack()
    username_entry = tk.Entry(signup_frame, borderwidth=3, relief="sunken")
    username_entry.pack()

    email_label = tk.Label(signup_frame, text="Email:", font=("Times New Roman", 18))
    email_label.pack(pady=(25,5))
    email_entry = tk.Entry(signup_frame, borderwidth=3, relief="sunken")
    email_entry.pack()

    password_label= tk.Label(signup_frame, text="Password:", font=("Times New Roman", 18))
    password_label.pack(pady=(25,5))
    password_entry= tk.Entry(signup_frame, show="*", borderwidth=3, relief="sunken")
    password_entry.pack()

    confirm_password_label= tk.Label(signup_frame, text="Confirm Password:", font=("Times New Roman", 18))
    confirm_password_label.pack(pady=(25,5))
    confirm_password_entry= tk.Entry(signup_frame, show="*", borderwidth=3, relief="sunken")
    confirm_password_entry.pack()

    phone_number_label= tk.Label(signup_frame, text="Phone Number:", font=("Times New Roman", 18))
    phone_number_label.pack(pady=(25,5))
    phone_number_entry= tk.Entry(signup_frame, borderwidth=3, relief="sunken")
    phone_number_entry.pack()

    account_type_label= tk.Label(signup_frame, text="Account Type:", font=("Times New Roman", 18))
    account_type_label.pack(pady=(25,5))
    account_type_selection = ttk.Combobox(signup_frame, values=["Manager", "Employee"])
    account_type_selection.pack(pady=(0,25))

    signup_btn = tk.Button(
        signup_frame,
        text="Sign Up",
        font=("Times New Roman", 18),
        borderwidth=5,
        command=lambda: signup_action(
            signup_frame,
            username_entry,
            email_entry,
            password_entry,
            confirm_password_entry,
            phone_number_entry,
            account_type_selection
        )
    )
    signup_btn.pack(pady=(25,0), anchor="center")

    home_btn = tk.Button(
        signup_frame,
        text="Home",
        font=("Times New Roman", 18),
        borderwidth=5,
        command=lambda: return_home(signup_frame)
    )
    home_btn.pack(pady=(25,0), anchor="center")

def signup_action(signup_frame, username_entry, email_entry, password_entry, confirm_password_entry, phone_number_entry, account_type_selection):
    username = username_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    phone_number = phone_number_entry.get()
    account_type = account_type_selection.get()

    if not username or not email or not password or not confirm_password or not phone_number or not account_type:
        tk.messagebox.showinfo(title="Error", message="Please fill in all fields.")
        return

    if password != confirm_password:
        tk.messagebox.showinfo(title="Error", message="Passwords do not match.")
        return

    if get_user(username):
        tk.messagebox.showinfo(title="Error", message="Username already exists.")
        return

    try:
        add_user(username, email, password, phone_number, account_type)
        tk.messagebox.showinfo(title="Success", message="Account created successfully.")
        signup_frame.pack_forget()
        login()
    except Exception as e:
        tk.messagebox.showinfo(title="Error", message=f"An error occurred: {e}")

def return_home(current_frame):
    current_frame.pack_forget()
    main_label.pack(pady=(375,0), anchor="center")
    button_frame.pack(pady=(25, 0), anchor="center")

def login():
    main_label.pack_forget()
    button_frame.pack_forget()

    login_frame = tk.Frame()
    login_frame.pack(anchor="center")

    login_label = tk.Label(login_frame, text="Login", font=("Times New Roman", 24))
    login_label.pack(pady=(250,75), anchor="center")

    username_label = tk.Label(login_frame, text="Username:", font=("Times New Roman", 18))
    username_label.pack(pady=(25,5))
    username_entry = tk.Entry(login_frame, borderwidth=3, relief="sunken")
    username_entry.pack()

    password_label= tk.Label(login_frame, text="Password:", font=("Times New Roman", 18))
    password_label.pack(pady=(25,5))
    password_entry= tk.Entry(login_frame, show="*", borderwidth=3, relief="sunken")
    password_entry.pack()

    login_btn = tk.Button(
        login_frame,
        text="Login",
        font=("Times New Roman", 18),
        borderwidth=5,
        command=lambda: login_action(username_entry, password_entry, login_frame)
    )
    login_btn.pack(pady=(25,0), anchor="center")

    home_btn = tk.Button(
        login_frame,
        text="Home",
        font=("Times New Roman", 18),
        borderwidth=5,
        command=lambda: return_home(login_frame)
    )
    home_btn.pack(pady=(25, 0), anchor="center")

def login_action(username_entry, password_entry, login_frame):
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        tk.messagebox.showinfo(title="Error", message="Please fill in all fields.")
        return
    else:
        user = get_user(username)
        if user and user[3] == password:
            tk.messagebox.showinfo(title="Success", message="Login successful.")
            login_frame.pack_forget()
            dashboard(username)
        else:
            tk.messagebox.showinfo(title="Error", message="Invalid username or password.")

def dashboard(username):
    dashboard_frame = tk.Frame()
    dashboard_frame.pack()

    dashboard_label = tk.Label(dashboard_frame, text=f"Welcome back, {username}", font=("Times New Roman", 24))
    dashboard_label.pack(pady=(25,0), anchor="center")
    
    message_label = tk.Label(dashboard_frame, text="What do you want to do?", font=("Times New Roman", 18))
    message_label.pack(pady=(25,0), anchor="center")

root = tk.Tk()
root.title("SmartSeater")
root.state("zoomed")

main_label = tk.Label(text="Welcome to SmartSeater", font=("Times New Roman", 24))
main_label.pack(pady=(375,0), anchor="center")

button_frame = tk.Frame()
button_frame.pack(pady=(25,0), anchor="center")

login_btn = tk.Button(
    button_frame,
    text="Login",
    font=("Times New Roman", 18),
    borderwidth=5,
    command=login
)
login_btn.pack(anchor="center", side=tk.LEFT, padx=(0, 5))


signup_btn = tk.Button(
    button_frame,
    text="Sign Up",
    font=("Times New Roman", 18),
    borderwidth=5,
    command=signup
)
signup_btn.pack(anchor="center", side=tk.LEFT, padx=(5, 0))

root.mainloop()