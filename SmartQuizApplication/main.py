
import tkinter as tk
from tkinter import ttk, messagebox

# Quiz question database
QUIZ_DATA = {
    "Python": [
        {
            "question": "Which keyword is used to define a function?",
            "options": ["func", "def", "function", "define"],
            "answer": "def"
        },
        {
            "question": "Which data type stores key-value pairs?",
            "options": ["List", "Tuple", "Dictionary", "Set"],
            "answer": "Dictionary"
        },
        {
            "question": "Which symbol starts a comment in Python?",
            "options": ["//", "#", "/*", "--"],
            "answer": "#"
        },
        {
            "question": "Which loop iterates over a sequence?",
            "options": ["if", "for", "def", "class"],
            "answer": "for"
        },
        {
            "question": "Which function displays output?",
            "options": ["input()", "show()", "print()", "display()"],
            "answer": "print()"
        }
    ],

    "Computer Science": [
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Control Processing User"
            ],
            "answer": "Central Processing Unit"
        },
        {
            "question": "Which structure follows FIFO?",
            "options": ["Stack", "Queue", "Tree", "Graph"],
            "answer": "Queue"
        },
        {
            "question": "Which language is commonly used for web styling?",
            "options": ["HTML", "CSS", "SQL", "Python"],
            "answer": "CSS"
        },
        {
            "question": "Which of these is an operating system?",
            "options": ["MySQL", "Windows", "HTML", "Java"],
            "answer": "Windows"
        },
        {
            "question": "What does RAM stand for?",
            "options": [
                "Read Access Memory",
                "Random Access Memory",
                "Run All Memory",
                "Rapid Action Module"
            ],
            "answer": "Random Access Memory"
        }
    ],

    "General Knowledge": [
        {
            "question": "What is the capital of India?",
            "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
            "answer": "New Delhi"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Venus", "Mars", "Jupiter"],
            "answer": "Mars"
        },
        {
            "question": "How many days are there in a leap year?",
            "options": ["364", "365", "366", "367"],
            "answer": "366"
        },
        {
            "question": "Which is the largest ocean on Earth?",
            "options": [
                "Atlantic Ocean",
                "Indian Ocean",
                "Arctic Ocean",
                "Pacific Ocean"
            ],
            "answer": "Pacific Ocean"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"],
            "answer": "Carbon dioxide"
        }
    ]
}





# Create the application class

class SmartQuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Quiz Application")
        self.root.geometry("750x550")
        self.root.minsize(600, 450)
        self.root.configure(bg="#F2F5FA")

        self.category = tk.StringVar(value="Python")
        self.selected_answer = tk.StringVar(value="")

        self.questions = []
        self.current_question = 0
        self.score = 0
        self.answers = []

        self.setup_home()

    def setup_home(self):
        self.clear_window()

        title = tk.Label(
            self.root,
            text="SMART QUIZ APPLICATION",
            font=("Arial", 23, "bold"),
            bg="#F2F5FA",
            fg="#17365D"
        )
        title.pack(pady=(35, 10))

        subtitle = tk.Label(
            self.root,
            text="Test your knowledge and improve your skills!",
            font=("Arial", 12),
            bg="#F2F5FA"
        )
        subtitle.pack(pady=5)

        tk.Label(
            self.root,
            text="Select a Quiz Category",
            font=("Arial", 13, "bold"),
            bg="#F2F5FA"
        ).pack(pady=(35, 10))

        self.category_box = ttk.Combobox(
            self.root,
            textvariable=self.category,
            values=list(QUIZ_DATA.keys()),
            state="readonly",
            font=("Arial", 12),
            width=28
        )
        self.category_box.pack(pady=5)

        tk.Button(
            self.root,
            text="Start Quiz",
            command=self.start_quiz,
            font=("Arial", 13, "bold"),
            bg="#17365D",
            fg="white",
            activebackground="#254D7A",
            activeforeground="white",
            width=18,
            pady=8,
            cursor="hand2"
        ).pack(pady=25)

        tk.Label(
            self.root,
            text="15 questions available across 3 categories",
            font=("Arial", 10),
            bg="#F2F5FA",
            fg="#555555"
        ).pack(pady=5)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
# Start the quiz

    def start_quiz(self):
        self.questions = QUIZ_DATA[self.category.get()].copy()

        self.current_question = 0
        self.score = 0
        self.answers = []

        self.setup_quiz_screen()
        self.show_question()

    def setup_quiz_screen(self):
        self.clear_window()

        self.header = tk.Label(
            self.root,
            text="SMART QUIZ",
            font=("Arial", 20, "bold"),
            bg="#F2F5FA",
            fg="#17365D"
        )
        self.header.pack(pady=15)

        self.progress_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            bg="#F2F5FA"
        )
        self.progress_label.pack(pady=5)

        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=500,
            mode="determinate",
            maximum=len(self.questions)
        )
        self.progress.pack(pady=8)

        self.question_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 15, "bold"),
            wraplength=620,
            justify="left",
            bg="#F2F5FA",
            fg="#222222"
        )
        self.question_label.pack(
            anchor="w",
            padx=55,
            pady=(25, 15)
        )

        self.options_frame = tk.Frame(
            self.root,
            bg="#F2F5FA"
        )
        self.options_frame.pack(
            fill="x",
            padx=55,
            pady=5
        )

        self.feedback_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 11),
            bg="#F2F5FA"
        )
        self.feedback_label.pack(pady=8)

        self.next_button = tk.Button(
            self.root,
            text="Submit Answer",
            command=self.submit_answer,
            font=("Arial", 12, "bold"),
            bg="#17365D",
            fg="white",
            width=18,
            pady=7
        )
        self.next_button.pack(pady=12)

    def show_question(self):
        question_data = self.questions[self.current_question]

        self.selected_answer.set("")
        self.feedback_label.config(text="", fg="#222222")

        self.progress_label.config(
            text=(
                f"Category: {self.category.get()}   |   "
                f"Question {self.current_question + 1} "
                f"of {len(self.questions)}   |   "
                f"Remaining: {len(self.questions) - self.current_question}"
            )
        )

        self.progress["value"] = self.current_question

        self.question_label.config(
            text=question_data["question"]
        )

        for widget in self.options_frame.winfo_children():
            widget.destroy()

        for option in question_data["options"]:
            tk.Radiobutton(
                self.options_frame,
                text=option,
                variable=self.selected_answer,
                value=option,
                font=("Arial", 12),
                bg="#F2F5FA",
                activebackground="#F2F5FA",
                anchor="w",
                justify="left",
                wraplength=570,
                padx=8,
                pady=7
            ).pack(fill="x", anchor="w")

        self.next_button.config(
            text="Submit Answer",
            state="normal",
            command=self.submit_answer
        )


# Check answers and calculate scores

    def submit_answer(self):
        chosen = self.selected_answer.get()

        if not chosen:
            messagebox.showwarning(
                "No Answer",
                "Please select an answer before continuing."
            )
            return

        question_data = self.questions[self.current_question]
        correct_answer = question_data["answer"]

        is_correct = chosen == correct_answer

        if is_correct:
            self.score += 1
            self.feedback_label.config(
                text="Correct answer!",
                fg="green"
            )
        else:
            self.feedback_label.config(
                text=f"Incorrect. Correct answer: {correct_answer}",
                fg="red"
            )

        self.answers.append({
            "question": question_data["question"],
            "chosen": chosen,
            "correct": correct_answer,
            "is_correct": is_correct
        })

        self.next_button.config(
            text="Next Question",
            command=self.next_question
        )

    def next_question(self):
        self.current_question += 1

        if self.current_question < len(self.questions):
            self.show_question()
        else:
            self.show_results()
# Display final results


    def show_results(self):
        self.clear_window()

        total = len(self.questions)
        incorrect = total - self.score
        percentage = (self.score / total) * 100 if total else 0

        if percentage >= 80:
            performance = "Excellent performance!"
        elif percentage >= 60:
            performance = "Good job! Keep practising."
        elif percentage >= 40:
            performance = "Fair result. More practice will help."
        else:
            performance = "Keep learning and try again!"

        tk.Label(
            self.root,
            text="QUIZ COMPLETED!",
            font=("Arial", 23, "bold"),
            bg="#F2F5FA",
            fg="#17365D"
        ).pack(pady=(20, 10))

        tk.Label(
            self.root,
            text=f"Category: {self.category.get()}",
            font=("Arial", 12),
            bg="#F2F5FA"
        ).pack(pady=3)

        tk.Label(
            self.root,
            text=f"Your Score: {self.score} / {total}",
            font=("Arial", 20, "bold"),
            bg="#F2F5FA",
            fg="#17365D"
        ).pack(pady=8)

        tk.Label(
            self.root,
            text=f"Percentage: {percentage:.1f}%",
            font=("Arial", 15),
            bg="#F2F5FA"
        ).pack(pady=3)

        tk.Label(
            self.root,
            text=f"Correct: {self.score}    Incorrect: {incorrect}",
            font=("Arial", 12),
            bg="#F2F5FA"
        ).pack(pady=5)

        tk.Label(
            self.root,
            text=performance,
            font=("Arial", 13, "bold"),
            bg="#F2F5FA",
            fg="#238636"
        ).pack(pady=8)

        tk.Label(
            self.root,
            text="Answer Review",
            font=("Arial", 14, "bold"),
            bg="#F2F5FA"
        ).pack(pady=(8, 4))

        review_frame = tk.Frame(self.root, bg="#F2F5FA")
        review_frame.pack(fill="both", expand=True, padx=25, pady=5)

        scrollbar = ttk.Scrollbar(review_frame)
        scrollbar.pack(side="right", fill="y")

        review = tk.Text(
            review_frame,
            height=8,
            font=("Arial", 10),
            wrap="word",
            yscrollcommand=scrollbar.set
        )
        review.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=review.yview)

        for number, answer in enumerate(self.answers, start=1):
            status = "Correct" if answer["is_correct"] else "Incorrect"

            review.insert(
                "end",
                f"{number}. {answer['question']}\n"
                f"Your answer: {answer['chosen']}\n"
                f"Correct answer: {answer['correct']}\n"
                f"Result: {status}\n\n"
            )

        review.config(state="disabled")

        tk.Button(
            self.root,
            text="Try Again",
            command=self.setup_home,
            font=("Arial", 11, "bold"),
            bg="#17365D",
            fg="white",
            width=16,
            pady=6
        ).pack(pady=10)





# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = SmartQuizApp(root)
    root.mainloop()
