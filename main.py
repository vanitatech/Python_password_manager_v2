from tkinter import *
from pathlib import Path
import pyperclip 
from tkinter import messagebox
import random
import string
import json

data_path = Path(__file__).parent / "data.json"

window = Tk()
window.title("Password Manager")
canvas = Canvas(window, width=200, height=200)
canvas.grid(row=0, column=1)
window.config(padx=50, pady=50)


image_path = Path(__file__).parent / "logo.png"
logo_img = PhotoImage(file=str(image_path))
canvas.create_image(100, 100, image=logo_img)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def find_password():
    user_input = website_entry.get()
    try:
        with open(data_path, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror(title="Error", message="No Data file found")
    else:
        if user_input in data:
            email = data[user_input]["email"]
            password = data[user_input]["password"]
            messagebox.showinfo(title=f"{user_input}", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="No details for the website exists")
        website_entry.delete(0, END)




# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    password = ''.join(random.choices(string.ascii_letters 
                                      + string.digits 
                                      + string.punctuation, k=12))
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

# Save password
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!") 
        return
    else:
        try:
            with open(data_path, "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
                with open(data_path, "w") as file:
                    json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(data_path, "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #




# Label Website
website_label = Label(window, text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(window, width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

#Label Email/Username
email_label = Label(window, text="Email/Username: ")
email_label.grid(row=2, column=0)
email_entry = Entry(window, width=36)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "vanita@example.com")

# Label Password
password_label = Label(window, text="Password: ")
password_label.grid(row=3, column=0)
password_entry = Entry(window, width=21)
password_entry.grid(row=3, column=1)

# Button Generate Password
generate_password_button = Button(window, text="Generate Password", width=14, font=("Ariel", 8), command=generate_password)
generate_password_button.grid(row=3, column=2)


#Button Add
add_button = Button(window, text="Add", width=33, command=save_password, pady=0)
add_button.grid(row=4, column=1, columnspan=2)

#Button Search
search_button = Button(window, text="Search", width=11, command=find_password, pady=0)
search_button.grid(row=1, column=2)




window.mainloop()