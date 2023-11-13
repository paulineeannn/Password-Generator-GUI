from tkinter import StringVar, messagebox, END
import customtkinter
import random
import string
import pyperclip
from PIL import Image

def command_copy(password):
    # copy the generated password in clipboard
    pyperclip.copy(password)
    messagebox.showinfo("Password Generator", "Copied to clipboard")

def command_generateAgain(length, upper, lower, num, spec):
    # delete the content of textbox
    textbox.configure(state="normal")
    textbox.delete("1.0", END)

    # generate new password
    password = function_generate(length, upper, lower, num, spec)

    # insert the new password in the textbox
    textbox.insert("1.0", password)
    textbox.configure(state="disabled")

    # change the text to be copied in the copy button
    button_copy.configure(command=lambda: command_copy(password))

def command_generate():
    global textbox, button_copy

    # get the entered length
    length = slider_length.get()
    length = int(length)

    # get the checked characters
    upper = char_uppercase.get()
    lower = char_lowercase.get()
    num = char_num.get()
    spec = char_special.get()

    # close the home frame
    frame_home.destroy()

    # open generated password frame
    frame_generate = customtkinter.CTkFrame(window, width=350, height=600, fg_color="#B4C5E4")
    frame_generate.place(x=0, y=0)

    label_generated = customtkinter.CTkLabel(frame_generate, text="GENERATED\nPASSWORD:",
                                          font=("Century Gothic", 32, "bold"), justify="center", width=350,
                                          fg_color="transparent", text_color="#0F005B")
    label_generated.place(x=0, y=60)


    textbox = customtkinter.CTkTextbox(frame_generate, corner_radius=15,
                                       width=277, height=100,
                                       font=("Century Gothic", 18),
                                       text_color="#0F005B")
    textbox.place(x=36, y=145)

    # generate password
    password = function_generate(length, upper, lower, num, spec)

    # insert the generated password in the textbox
    textbox.insert("1.0", password)
    textbox.configure(state="disabled")

    button_copy = customtkinter.CTkButton(frame_generate,
                                          text="Copy",font=("Century Gothic", 19, "bold"),
                                          corner_radius=15, height=43, width=226,
                                          fg_color="#0F005B", hover_color="#403B5D",
                                          command=lambda: command_copy(password))
    button_copy.place(x=62, y=295)

    button_generateAgain = customtkinter.CTkButton(frame_generate,
                                                   text="Generate Again", font=("Century Gothic", 19),
                                                   corner_radius=15, height=43, width=226,
                                                   fg_color="#3066BE", hover_color="#403B5D",
                                                   command=lambda: command_generateAgain(length, upper, lower, num, spec))
    button_generateAgain.place(x=62, y=345)

    button_home = customtkinter.CTkButton(frame_generate,
                                          text="Home",
                                          font=("Century Gothic", 19),
                                          corner_radius=15, height=43, width=226,
                                          fg_color="#87A8DE", hover_color="#403B5D",
                                          command=command_home)
    button_home.place(x=62, y=395)

def function_generate(length, upper, lower, num, spec):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    specials = string.punctuation
    password = ''
    choices = []

    if upper == 'upper_yes':
        choices += uppercase

    if lower == 'lower_yes':
        choices += lowercase

    if num == 'num_yes':
        choices += numbers

    if spec == 'special_yes':
        choices += specials

    for x in range(length):
        password += random.choice(choices)

    return password

def command_home():
    display_home()

def display_home():
    global frame_home, slider_length, var_characters, char_uppercase, char_lowercase, char_num, char_special

    frame_home = customtkinter.CTkFrame(window, width=350, height=600, fg_color="#B4C5E4")
    frame_home.place(x=0, y=0)

    img_header = customtkinter.CTkImage(light_image=Image.open("../Password Generator/images/header.png"),
                                        size=(350, 69))

    label_header = customtkinter.CTkLabel(frame_home, image=img_header, text="")
    label_header.place(x=0, y=54)

    label_length = customtkinter.CTkLabel(frame_home, text="Length:",
                                          font=("Century Gothic", 25, "bold"),
                                          fg_color="transparent", text_color="#0F005B")
    label_length.place(x=75, y=150)


    slider_length = customtkinter.CTkSlider(frame_home, from_=4, to=30)
    slider_length.place(x=72, y=187)
    slider_length.set(8)

    slider_length_label = customtkinter.CTkLabel(frame_home, text="8", font=("Century Gothic", 25),
                                                 fg_color="transparent", text_color="#0F005B")
    slider_length_label.place(x=170, y=150)

    def on_slider_change(value):
        slider_length_label.configure(text=f"{int(value)}")

    slider_length.bind("<B1-Motion>", lambda event: on_slider_change(slider_length.get()))
    slider_length.bind("<ButtonRelease-1>", lambda event: on_slider_change(slider_length.get()))

    label_characters = customtkinter.CTkLabel(frame_home, text="Characters:",
                                          font=("Century Gothic", 25, "bold"),
                                          fg_color="transparent", text_color="#0F005B")
    label_characters.place(x=75, y=215)

    # Choice Check boxes
    var_characters = StringVar(value="Choice 1")

    char_uppercase = customtkinter.CTkCheckBox(frame_home, text="Uppercase Letters",
                                               font=("Century Gothic", 18), variable=var_characters,
                                               text_color="#0F005B", fg_color="#3066BE",
                                               onvalue="upper_yes", offvalue="upper_no")
    char_uppercase.place(x=75, y=255)

    char_lowercase = customtkinter.CTkCheckBox(frame_home, text="Lowercase Letters",
                                               font=("Century Gothic", 18), variable=var_characters,
                                               text_color="#0F005B", fg_color="#3066BE",
                                               onvalue="lower_yes", offvalue="lower_no")
    char_lowercase.place(x=75, y=290)
    char_lowercase.select(1)

    char_num = customtkinter.CTkCheckBox(frame_home, text="Numbers",
                                         font=("Century Gothic", 18), variable=var_characters,
                                         text_color="#0F005B", fg_color="#3066BE",
                                         onvalue="num_yes", offvalue="num_no")
    char_num.place(x=75, y=325)

    char_special = customtkinter.CTkCheckBox(frame_home, text="Special Characters",
                                             font=("Century Gothic", 18), variable=var_characters,
                                             text_color="#0F005B", fg_color="#3066BE",
                                             onvalue="special_yes", offvalue="special_no")
    char_special.place(x=75, y=360)

    button_generate = customtkinter.CTkButton(frame_home,
                                              text="Generate",
                                              font=("Century Gothic", 20, "bold"),
                                              corner_radius=15,
                                              height=43, width=226,
                                              fg_color="#0F005B",
                                              hover_color="#190096",
                                              command=command_generate)
    button_generate.place(x=62, y=424)

    window.mainloop()


if __name__ == "__main__":
    # create window and configure its properties
    window = customtkinter.CTk(fg_color="#B4C5E4")
    window.title("Password Generator")

    # get the user's screen size
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the center coordinates
    center_x = int((screen_width - 50) / 2)
    center_y = int((screen_height - 600) / 2)

    window.geometry(f"350x600+{center_x}+{center_y}")
    window.resizable(0, 0)
    icon = "../Password Generator/images/passwordGen.ico"
    window.iconbitmap(icon)

    display_home()
