#IMPORT TKINTER
from tkinter import *
from tkinter import ttk
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
style = ttk.Style()
style.configure("Default", foreground="white", background="blue", font=("Arial", 12, "bold"))

#The Dashboard is organized into the following widgets:
#1. Welcome Label
label = ttk.Label(root, text="Welcome to ShookNamer!", style="Default")
label.pack(pady=20)  # Use pack geometry manager to place the label

#2. User Profile Button
user_profile = ttk.Button(root, text=f"User Profile: {username}", style = "Default", command=open_user_profile)
user_profile.pack(pady=20)

#2a. User Profile opens a user profile popup
def open_user_profile():
  user_profile_popup = TopLevel(root)
  user_profile_popup.title(f"{username} Profile")
  
  signout_button = ttk.Button(user_profile_popup, text="Sign out", style = "Default", command=sign_out)
  signout_button.pack(pady=20)

def sign_out():
  user_profile_popup.destroy()
  shooknamer_login()
  
#MATTER LISTBOX

matter_listbox = ttk.Listbox(root, height=40, width=40)
matter_listbox.pack(pady=20)

def get_matter_list():
  matter_listbox.delete(0, END)
  for matter_profile in matter_profiles
    matter_listbox.insert(END, f"{matter_profile}.txt")

#CREATE MATTER PROFILE BUTTON
matter_button = ttk.Button(root, text="Create Matter Profile", style="Default", command=create_matter_profile)
matter_button.pack(pady=20)

def create_matter_profile():
  def create_new_matter_profile():
    plaintiff_name = plaintiff_name_entry.get()
    defendant_name = defendant_name_entry.get()

    matter_profile_path = os.path.join(f"{user_dir}", "matter_profiles", f"{defendant_name_entry}")
    if os.path.exists(matter_profile_path):
      print(f"{matter_profile_path} already exists!") 
    else:
      os.makedirs(matter_profile_path)
      
      plaintiff_profile_path = os.path.join (f"user_dir", "matter_profiles", f"{defendant_name_entry}.txt")
      if os.path.exists(plaintiff_profile_path):
        print(f"{plaintiff_profile_path} already exists!")
      else: 
        open(plaintiff_profile_path, "w") as file:
          file.write(f"Plaintiff Name: {plaintiff_name_entry}")
          file.write(f"Defendant Name: {defendant_name_entry}")
          os.rename(matter_profile_path, f"{plaintiff_name_entry}")

  create_matter_profile_popup = TopLevel(root)
  create_matter_profile_popup.title("Create Matter Profile")
  create_matter_profile_popup.geometry("300x300")

  plaintiff_name_label = ttk.Label(create_matter_profile_popup, text="Plaintiff Name", style="Default")
  plaintiff_name_label.pack(pady=20)
  plaintiff_name_entry = ttk.Entry(create_matter_profile_popup)
  plaintiff_name_entry.pack(pady=20)

  defendant_name_label = ttk.Label(create_matter_profile_popup, text="Defendant Name", style="Default")
  defendant_name_label.pack(pady=20)
  defendant_name_entry = ttk.Entry(create_matter_profile_popup)
  defendant_name_entry.pack(pady=20)

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
        
  popup = TopLevel(root)
  popup.title("ShookNamer Login")
  popup.geometry("300x300")

  username_label = ttk.Label(popup, text="Username", style="Default")
  username_label.pack(pady=20)
  username_entry = ttk.Entry(popup)
  username_entry.pack(pady=20)
  password_label = ttk.Label(popup, text="Password", style="Default")
  password_label.pack(pady=20)
  password_entry = ttk.Entry(popup, show="*")
  login_button = ttk.Button(popup, text="Login", command=lambda: login(username_entry.get(), password_entry.get()))

#CREATE DIRECTORY FOR USER
def create_user_dir(username):
  current_dir = os.getcwd()
  user_dir = f"{username}"
  path = os.path.join (current_dir, user_dir)

  try:
    os.makedirs(path)
  except FileExistsError:
    print(f"Directory '{user_dir}' already exists at {current_dir}.")
  except Exception as e:
    print(f"Error creating directory '{user_dir}': {e}")

  #CREATE SUBFOLDERS
  subfolders = ["matter_profiles",] #Subfolders list
  for folder in subfolders:
      subfolder_path = os.path.join(path, folder)
      try:
        os.makedirs(subfolder_path)
        print(f"Subfolders successfuly created in {path}.")
      except FileExistsError:
        print(f"Subfolders alread yexist in {path}.")
      except Exception as e:
        print(f"Error creating subfolders in {path}: {e}.")

#RUN PROGRAM

#Login Please
shooknamer_login()

#DASHBOARD
root.mainloop()
