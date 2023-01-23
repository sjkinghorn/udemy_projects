from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def change_word():
    global current_card, flip_timer
    root.after_cancel(flip_timer)
    current_card = choice(to_learn)
    flashcard.itemconfig(language_text, fill="black", text="French")
    flashcard.itemconfig(word_text, fill="black", text=current_card["French"])
    flashcard.itemconfig(flashcard_image, image=card_front)
    flip_timer = root.after(3000, func=flip_card)


def flip_card():
    flashcard.itemconfig(language_text, fill="white", text="English")
    flashcard.itemconfig(word_text, fill="white", text=current_card["English"])
    flashcard.itemconfig(flashcard_image, image=card_back)


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    change_word()


root = Tk()
root.title("Flashcard App")
root.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = root.after(3000, func=flip_card)

flashcard = Canvas(width=800, height=526)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
flashcard_image = flashcard.create_image(400, 263, image=card_front)
flashcard.config(bg=BACKGROUND_COLOR, highlightthickness=0)
language_text = flashcard.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, 'italic'))
word_text = flashcard.create_text(400, 250, text="word", fill="black", font=("Ariel", 60, 'bold'))
flashcard.grid(row=0, column=0, columnspan=2)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=change_word)
wrong_button.grid(row=1, column=0)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, relief="flat", bg=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)

change_word()

root.mainloop()
