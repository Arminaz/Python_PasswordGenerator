# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    # Getting inputs
    website = website_input.get()
    username = email_user_input.get()
    password = password_input.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops" message="Please do not leave any empty fields!")
        return

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {username}\nPassword: {password}\n Is it ok to save?")

    if is_ok:
        # Putting inputs in the file
        with open(file="data.txt", mode="a") as file:
            file.write(f"{website} | {username} | {password}\n")
        
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
generate_password = Button(text="Generate Password")
add_button = Button(width=36, text="Add", command=save)

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