#IMPORT TKINTER
from tkinter import *
import json
import os

username = None
user_dir = None
matter_profiles = []

#CREATE ROOT WIDGET
root = Tk()
root.title("ShookNamer")

#WINDOW SIZING
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")

#SET DEFAULT STYLE
default_font = ("Arial", 12, "bold")

#The Dashboard is organized into the following widgets:
#1. Welcome Label
label = Label(root, text="Welcome to ShookNamer!", fg="white", bg="blue", font=default_font)
label.pack(pady=20)  # Use pack geometry manager to place the label

#2. User Profile Button
def open_user_profile():
    user_profile_popup = Toplevel(root)
    user_profile_popup.title(f"{username} Profile")

    signout_button = Button(user_profile_popup, text="Sign out", fg="white", bg="blue", font=default_font, command=lambda: sign_out(user_profile_popup))
    signout_button.pack(pady=20)

user_profile = Button(root, text=f"User Profile: {username}", fg="white", bg="blue", font=default_font, command=open_user_profile)
user_profile.pack(pady=20)

#2a. User Profile opens a user profile popup
def sign_out(user_profile_popup):
    user_profile_popup.destroy()
    shooknamer_login()

#MATTER LISTBOX

matter_listbox = Listbox(root, height=40, width=40)
matter_listbox.pack(pady=20)

def get_matter_list():
    matter_listbox.delete(0, END)
    for matter_profile in matter_profiles:
        matter_listbox.insert(END, f"{matter_profile}.txt")

#CREATE MATTER PROFILE BUTTON
def create_matter_profile():
    def create_new_matter_profile():
        plaintiff_name = plaintiff_name_entry.get()
        defendant_name = defendant_name_entry.get()

        matter_profile_path = os.path.join(user_dir, "matter_profiles", defendant_name)
        if os.path.exists(matter_profile_path):
            print(f"{matter_profile_path} already exists!") 
        else:
            os.makedirs(matter_profile_path)

            plaintiff_profile_path = os.path.join(user_dir, "matter_profiles", defendant_name, f"{plaintiff_name}.txt")
            if os.path.exists(plaintiff_profile_path):
                print(f"{plaintiff_profile_path} already exists!")
            else: 
                with open(plaintiff_profile_path, "w") as file:
                    file.write(f"Plaintiff Name: {plaintiff_name}\n")
                    file.write(f"Defendant Name: {defendant_name}")
                os.rename(matter_profile_path, os.path.join(user_dir, "matter_profiles", defendant_name, f"{plaintiff_name}.txt"))

    create_matter_profile_popup = Toplevel(root)
    create_matter_profile_popup.title("Create Matter Profile")
    create_matter_profile_popup.geometry("300x300")

    plaintiff_name_label = Label(create_matter_profile_popup, text="Plaintiff Name", fg="white", bg="blue", font=default_font)
    plaintiff_name_label.pack(pady=20)
    plaintiff_name_entry = Entry(create_matter_profile_popup)
    plaintiff_name_entry.pack(pady=20)

    defendant_name_label = Label(create_matter_profile_popup, text="Defendant Name", fg="white", bg="blue", font=default_font)
    defendant_name_label.pack(pady=20)
    defendant_name_entry = Entry(create_matter_profile_popup)
    defendant_name_entry.pack(pady=20)

    create_button = Button(create_matter_profile_popup, text="Create", fg="white", bg="blue", font=default_font, command=create_new_matter_profile)
    create_button.pack(pady=20)

matter_button = Button(root, text="Create Matter Profile", fg="white", bg="blue", font=default_font, command=create_matter_profile)
matter_button.pack(pady=20)

#USER DICTIONARY
try:
    with open("users.json", "r") as file:
        users = json.load(file)
except FileNotFoundError:
    users = {}

def save_users():
    with open("users.json", "w") as file:
        json.dump(users, file)

#LOGIN POPUP
def shooknamer_login():
    def login(username, password):
        if username in users and users[username] == password:
            print("Login Successful!")
            popup.destroy()
            create_user_dir(username)
        else:
            print("Login failed. Invalid username or password.")

    popup = Toplevel(root)
    popup.title("ShookNamer Login")
    popup.geometry("300x300")

    username_label = Label(popup, text="Username", fg="white", bg="blue", font=default_font)
    username_label.pack(pady=20)
    username_entry = Entry(popup)
    username_entry.pack(pady=20)
    password_label = Label(popup, text="Password", fg="white", bg="blue", font=default_font)
    password_label.pack(pady=20)
    password_entry = Entry(popup, show="*")
    password_entry.pack(pady=20)
    login_button = Button(popup, text="Login", fg="white", bg="blue", font=default_font, command=lambda: login(username_entry.get(), password_entry.get()))
    login_button.pack(pady=20)

#CREATE DIRECTORY FOR USER
def create_user_dir(username):
    global user_dir
    user_dir = os.path.join(os.getcwd(), username)

    try:
        os.makedirs(user_dir)
    except FileExistsError:
        print(f"Directory '{user_dir}' already exists.")
    except Exception as e:
        print(f"Error creating directory '{user_dir}': {e}")

    #CREATE SUBFOLDERS
    subfolders = ["matter_profiles",] #Subfolders list
    for folder in subfolders:
        subfolder_path = os.path.join(user_dir, folder)
        try:
            os.makedirs(subfolder_path)
            print(f"Subfolders successfully created in {user_dir}.")
        except FileExistsError:
            print(f"Subfolders already exist in {user_dir}.")
        except Exception as e:
            print(f"Error creating subfolders in {user_dir}: {e}.")
        
    get_matter_list()

#RUN PROGRAM

#Login Please
shooknamer_login()

#DASHBOARD
root.mainloop()
