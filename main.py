# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
            'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
            'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_list = []

    password_list.extend(choice(letters) for _ in range(nr_letters))
    password_list.extend(choice(symbols) for _ in range(nr_symbols))
    password_list.extend(choice(numbers) for _ in range(nr_numbers))

    shuffle(password_list)

    password = "".join(password_list)
    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Getting inputs
    website = website_input.get()
    email = email_user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please do not leave any empty fields!")
        return

    # Reading the existing data
    with open(file="data.json", mode="r") as file:
        data = json.load(file)
        data.update(new_data)
    
    # Writing to the file
    with open(file="data.json", mode="w") as file:
        json.dump(data, file, indent=4)
    
    # Clear Output
    website_input.delete(0, END)
    email_user_input.delete(0, END)
    email_user_input.insert(0, "email@example.com")
    password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40, bg="#ffffff")

# Canvas Image
canvas = Canvas(width=200, height=200, bg="#ffffff", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=2, row=1)


# Form
# # Labels
website_label = Label(text="Website:", bg="#ffffff")
email_user_label = Label(text="Email/Username:", bg="#ffffff")
password_label = Label(text="Password:", bg="#ffffff")

# # Inputs / Entry
website_input = Entry(width=39)
email_user_input = Entry(width=39)
password_input = Entry(width=21)

# # Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
add_button = Button(width=36, text="Add", command=save)

# # Grid Placement
website_label.grid(column=1, row=2)
website_input.grid(column=2, row=2, columnspan=2)

email_user_label.grid(column=1, row=3)
email_user_input.grid(column=2, row=3, columnspan=2)

password_label.grid(column=1, row=4)
password_input.grid(column=2, row=4)
generate_password_button.grid(column=3, row=4)

add_button.grid(column=2, row=5, columnspan=2)

# # Config Options
website_input.focus()
email_user_input.insert(0, "email@example.com")



window.mainloop()