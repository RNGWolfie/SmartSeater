import os
import base64
import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import add_user, get_user, delete_user

class Login:
    def __init__(self, root, main_label, button_frame):
        self.root = root
        self.main_label = main_label
        self.button_frame = button_frame
        self.login_frame = tk.Frame(self.root)
        self.build_login_ui()
        
    def build_login_ui(self):
        self.main_label.pack_forget()
        self.button_frame.pack_forget()

        self.login_frame.pack(anchor="center")

        login_label = tk.Label(self.login_frame, text="Login", font=("Times New Roman", 24))
        login_label.pack(pady=(250,75), anchor="center")

        username_label = tk.Label(self.login_frame, text="Username:", font=("Times New Roman", 18))
        username_label.pack(pady=(25,5))
        username_entry = tk.Entry(self.login_frame, borderwidth=3, relief="sunken")
        username_entry.pack()

        password_label= tk.Label(self.login_frame, text="Password:", font=("Times New Roman", 18))
        password_label.pack(pady=(25,5))
        password_entry= tk.Entry(self.login_frame, show="*", borderwidth=3, relief="sunken")
        password_entry.pack()

        login_btn = tk.Button(
            self.login_frame,
            text="Login",
            font=("Times New Roman", 18),
            borderwidth=5,
            command=lambda: self.login_action(username_entry, password_entry, self.login_frame)
        )
        login_btn.pack(pady=(25,0), anchor="center")

        home_btn = tk.Button(
            self.login_frame,
            text="Home",
            font=("Times New Roman", 18),
            borderwidth=5,
            command=lambda: return_home(self.login_frame, self.main_label, self.button_frame)
        )
        home_btn.pack(pady=(25, 0), anchor="center")

    def login_action(self, username_entry, password_entry, login_frame):
        username = username_entry.get()
        password = password_entry.get()

        if not username or not password:
            tk.messagebox.showinfo(title="Error", message="Please fill in all fields.")
            return
    
        else:
            user = get_user(username)
            if user and PasswordManager.verify_password(password, user[3]):
                if user[5] == "Employee":
                    tk.messagebox.showinfo(title="Success", message="Login successful.")
                    login_frame.pack_forget()
                    Dashboards.employee_dashboard(username)
                elif user[5] == "Manager":
                    tk.messagebox.showinfo(title="Success", message="Login successful.")
                    login_frame.pack_forget()
                    Dashboards.manager_dashboard(username)
                elif user[5] == "Customer":
                    tk.messagebox.showinfo(title="Success", message="Login successful.")
                    login_frame.pack_forget()
                    Dashboards.customer_dashboard(username)
                elif user[5] == "Applicant":
                    tk.messagebox.showinfo(title="Success", message="Login successful.")
                    login_frame.pack_forget()
                    Dashboards.applicant_dashboard(username)
            else:
                tk.messagebox.showinfo(title="Error", message="Invalid username or password.")

class Signup:
    def __init__(self, root, main_label, button_frame):
        self.root = root
        self.main_label = main_label
        self.button_frame = button_frame
        self.signup_frame = tk.Frame(self.root)
        self.build_signup_ui()

    def build_signup_ui(self):
        self.main_label.pack_forget()
        self.button_frame.pack_forget()

        self.signup_frame.pack(anchor="center")

        signup_label = tk.Label(self.signup_frame, text="Signup", font=("Times New Roman", 24))
        signup_label.pack(pady=(100,75), anchor="center")

        username_label = tk.Label(self.signup_frame, text="Username:", font=("Times New Roman", 18))
        username_label.pack()
        username_entry = tk.Entry(self.signup_frame, borderwidth=3, relief="sunken")
        username_entry.pack()

        email_label = tk.Label(self.signup_frame, text="Email:", font=("Times New Roman", 18))
        email_label.pack(pady=(25,5))
        email_entry = tk.Entry(self.signup_frame, borderwidth=3, relief="sunken")
        email_entry.pack()

        password_label= tk.Label(self.signup_frame, text="Password:", font=("Times New Roman", 18))
        password_label.pack(pady=(25,5))
        password_entry= tk.Entry(self.signup_frame, show="*", borderwidth=3, relief="sunken")
        password_entry.pack()

        confirm_password_label= tk.Label(self.signup_frame, text="Confirm Password:", font=("Times New Roman", 18))
        confirm_password_label.pack(pady=(25,5))
        confirm_password_entry= tk.Entry(self.signup_frame, show="*", borderwidth=3, relief="sunken")
        confirm_password_entry.pack()

        phone_number_label= tk.Label(self.signup_frame, text="Phone Number:", font=("Times New Roman", 18))
        phone_number_label.pack(pady=(25,5))
        phone_number_entry= tk.Entry(self.signup_frame, borderwidth=3, relief="sunken")
        phone_number_entry.pack()

        account_type_label= tk.Label(self.signup_frame, text="Account Type:", font=("Times New Roman", 18))
        account_type_label.pack(pady=(25,5))
        account_type_selection = ttk.Combobox(self.signup_frame, values=["Manager", "Employee", "Customer", "Applicant"])
        account_type_selection.pack(pady=(0,25))

        signup_btn = tk.Button(
            self.signup_frame,
            text="Sign Up",
            font=("Times New Roman", 18),
            borderwidth=5,
            command=lambda: self.signup_action(
                self.signup_frame,
                username_entry,
                email_entry,
                password_entry,
                confirm_password_entry,
                phone_number_entry,
                account_type_selection,
                self.main_label,
                self.button_frame
            )
        )
        signup_btn.pack(pady=(25,0), anchor="center")

        home_btn = tk.Button(
            self.signup_frame,
            text="Home",
            font=("Times New Roman", 18),
            borderwidth=5,
            command=lambda: return_home(self.signup_frame, self.main_label, self.button_frame)
        )
        home_btn.pack(pady=(25,0), anchor="center")

    def signup_action(self, signup_frame, username_entry, email_entry, password_entry, confirm_password_entry, phone_number_entry, account_type_selection, main_label, button_frame):
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
            hashed_password = PasswordManager.hash_password(password)
            add_user(username, email, hashed_password, phone_number, account_type)
            tk.messagebox.showinfo(title="Success", message="Account created successfully.")
            signup_frame.pack_forget()
            Login(self.root, main_label, button_frame)
        except Exception as e:
            tk.messagebox.showinfo(title="Error", message=f"An error occurred: {e}")

class PasswordManager:
    def hash_password(password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        storage = salt + key
        return base64.b64encode(storage).decode('utf-8')

    def verify_password(password, stored_password_hash):
        storage = base64.b64decode(stored_password_hash.encode('utf-8'))
        salt = storage[:32]
        stored_key = storage[32:]
        key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
        return key == stored_key

class Dashboards:
    def employee_dashboard(username):
        #TODO: Add employee dashboard code here
        pass

    def manager_dashboard(username):
        #TODO: Add manager dashboard code here
        pass

    def customer_dashboard(username):
        #TODO: Add customer dashboard code here
        pass

    def applicant_dashboard(username):
        #TODO: Add applicant dashboard code here
        pass

def return_home(current_frame, main_label, button_frame):
    current_frame.pack_forget()
    main_label.pack(pady=(375,0), anchor="center")
    button_frame.pack(pady=(25, 0), anchor="center")

def main():
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
        command= lambda: Login(root, main_label, button_frame)
    )
    login_btn.pack(anchor="center", side=tk.LEFT, padx=(0, 5))


    signup_btn = tk.Button(
        button_frame,
        text="Sign Up",
        font=("Times New Roman", 18),
        borderwidth=5,
         command= lambda: Signup(root, main_label, button_frame)
    )
    signup_btn.pack(anchor="center", side=tk.LEFT, padx=(5, 0))

    root.mainloop()

main()