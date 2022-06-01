from tkinter import *
from tkinter import messagebox
from random import shuffle, randint, choice
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']




    letter_list = [choice(letters) for _ in range(randint(8, 10))]
    symbol_list = [choice(symbols) for _ in range(randint(2, 4))]
    number_list = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = number_list + symbol_list + letter_list
    shuffle(password_list)
    password = "".join(password_list)
    pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    new_data = {
       website: {
        "email": email,
        "password": password,
        }
    }

    if len(website) == 0:
        messagebox.showinfo(title= "Warning", message="Don't leave any empty boxes!")
    elif len(password) == 0:
        messagebox.showinfo(title="Warning", message="Don't leave any empty boxes!")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            pass_entry.delete(0, END)


def search():
    website = web_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Warning", message="No data stored yet!")
    except KeyError:
        messagebox.showinfo(title="Warning", message="No website")
    else:
        messagebox.showinfo(title=website, message=f"Email {data[website]['email']}"
                                                   f"\nPassword:{data[website]['password']}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=35, pady=30)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_img)
canvas.grid(row=0, column=1)

# LABELS
web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
pass_label = Label(text="Password:")
pass_label.grid(column=0, row=3)

# ENTRIES
web_entry = Entry(width=33)
web_entry.grid(column=1, row=1, columnspan=1)
web_entry.focus()

email_entry = Entry(width=52)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,"arek.kubea@gmail.com")
pass_entry = Entry(width=33)
pass_entry.grid(column=1, row=3, columnspan=1)


# BUTTONS
gen_pass_button = Button(text="Generate Password", command=generate_password)
gen_pass_button.grid(column=2, row=3)
add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=5)
search_button = Button(text="Search", command=search, width=14)
search_button.grid(column=2, row=1, pady=3)


window.mainloop()