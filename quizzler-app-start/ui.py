from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 10, "bold"))
        self.score.grid(row=0, column=1)

        self.question_box = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.question_box.create_text(
            150,
            125,
            width=280,
            text="00:00",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"))
        self.question_box.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_guess)
        self.true_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_guess)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question_box.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.question_box.itemconfig(self.question_text, text=q_text)
        else:
            self.question_box.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_guess(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def false_guess(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.question_box.configure(bg="green")
        else:
            self.question_box.configure(bg="red")
        self.window.after(1000, self.get_next_question)
