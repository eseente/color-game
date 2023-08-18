import tkinter as tk
from random import randint


class ColorGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Renk Algılama Oyunu")

        self.colors = ["red", "green", "blue", "yellow", "purple", "orange"]
        self.score = 0
        self.time_left = 60
        self.game_mode = "normal"

        self.create_widgets()
        self.new_question()
        self.countdown()

    def create_widgets(self):
        self.color_text = tk.Label(self.master, font=("Helvetica", 60))
        self.color_text.pack(pady=30)

        self.answer_entry = tk.Entry(self.master, font=("Helvetica", 30))
        self.answer_entry.pack(pady=10)
        self.answer_entry.bind("<Return>", self.check_answer)

        self.score_label = tk.Label(self.master, text=f"Skor: {self.score}", font=("Helvetica", 20))
        self.score_label.pack()

        self.timer_label = tk.Label(self.master, text=f"Süre: {self.time_left}", font=("Helvetica", 20))
        self.timer_label.pack()

        self.mode_button = tk.Button(self.master, text="Mod Değiştir", font=("Helvetica", 14),
                                     command=self.change_game_mode)
        self.mode_button.pack(pady=10)

    def new_question(self):
        color = self.colors[randint(0, len(self.colors) - 1)]
        text = self.colors[randint(0, len(self.colors) - 1)]
        self.color_text.config(text=text, fg=color)

    def check_answer(self, event):
        answer = self.answer_entry.get().lower()
        self.answer_entry.delete(0, "end")
        if answer == self.color_text["fg"]:
            if self.game_mode == "reverse":
                self.score -= 1
            else:
                self.score += 1
            self.score_label.config(text=f"Skor: {self.score}")
            self.new_question()
        else:
            if self.score > 0:
                self.score -= 1
            self.score_label.config(text=f"Skor: {self.score}")

    def countdown(self):
        self.time_left -= 1
        self.timer_label.config(text=f"Süre: {self.time_left}")
        if self.time_left == 0:
            self.master.destroy()
        else:
            self.master.after(1000, self.countdown)

    def change_game_mode(self):
        if self.game_mode == "normal":
            self.game_mode = "reverse"
            self.mode_button.config(text="Ters Mod")
        else:
            self.game_mode = "normal"
            self.mode_button.config(text="Normal Mod")


root = tk.Tk()
game = ColorGame(root)
root.mainloop()
