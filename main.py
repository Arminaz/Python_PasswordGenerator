# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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
generate_password = Button(text="Generate Password")
add_button = Button(width=36, text="Add")

# # Grid Placement
website_label.grid(column=1, row=2)
website_input.grid(column=2, row=2, columnspan=2)

email_user_label.grid(column=1, row=3)
email_user_input.grid(column=2, row=3, columnspan=2)

password_label.grid(column=1, row=4)
password_input.grid(column=2, row=4)
generate_password.grid(column=3, row=4)

add_button.grid(column=2, row=5, columnspan=2)

# # Config Options
website_input.focus()
email_user_input.insert(0, "email@example.com")



window.mainloop()