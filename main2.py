#IMPORT TKINTER
from tkinter import *
from tkinter import ttk
import json
import os

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

#LABEL
label = ttk.Label(root, text="Welcome to ShookNamer!", style="Default")
label.pack(pady=20)  # Use pack geometry manager to place the label

matter_button = ttk.Button(root, text="Create Matter Profile", style="Default")



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
  subfolders = ["profiles",] #Subfolders list
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
