from tkinter import *
from pathlib import Path
import pyperclip 
from tkinter import messagebox
import random
import string

data_path = Path(__file__).parent / "data.txt"

window = Tk()
window.title("Password Manager")
canvas = Canvas(window, width=200, height=200)
canvas.grid(row=0, column=1)
window.config(padx=50, pady=50)


image_path = Path(__file__).parent / "logo.png"
logo_img = PhotoImage(file=str(image_path))
canvas.create_image(100, 100, image=logo_img)



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

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!") 
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")

        if is_ok and website and email and password:
            with open(data_path, "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #




# Label Website
website_label = Label(window, text="Website: ")
website_label.grid(row=1, column=0)

website_entry = Entry(window, width=36)
website_entry.grid(row=1, column=1, columnspan=2)
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




window.mainloop()