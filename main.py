from tkinter import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"
counter = 0
data = pandas.read_csv("words_to_learn.csv")
t_dict = data.to_dict(orient="records")

# Button Function ---------------------------------------------------
def wrong():
    next_card()
def right():
    global data, t_dict, counter
    data = data[data["French"] != data["French"][counter]]
    data.to_csv("words_to_learn.csv", index=False)
    data = pandas.read_csv("words_to_learn.csv")
    t_dict = data.to_dict(orient="records")
    counter = counter - 1
    next_card()
def next_card():
    global counter, flipMech
    window.after_cancel(flipMech)
    if counter == len(t_dict) - 1:
        counter = 0
    else:
        counter = counter + 1
    canvas.itemconfig(term_text, text=t_dict[counter]["French"], fill="black")
    canvas.itemconfig(lang_text, text="French", fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    flipMech = window.after(3000, func=flip)
def flip():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(term_text, text=t_dict[counter]["English"], fill="white")
    canvas.itemconfig(lang_text, text="English", fill="white")
# UI Design ----------------------------------------------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flipMech = window.after(3000, func=flip)
# Flash Card Generation
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
lang_text = canvas.create_text(400, 150, text="French", fill="black", font=("Ariel", 40, "italic"))
term_text = canvas.create_text(400, 263, text=t_dict[counter]["French"], fill="black", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button Generation
wrong_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=right)
right_button.grid(column=1, row=1)

# Ending Mechanism
window.mainloop()