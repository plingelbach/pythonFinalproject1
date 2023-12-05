import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from student_grader import StudentGrader
from student import Student


class StudentGraderGUI:
    def __init__(self):
        self.student_grader = StudentGrader()
        self.root = tk.Tk()
        self.root.title("Student Grader")

        self.students_entry = ttk.Entry(self.root)
        self.students_label = ttk.Label(self.root, text="Total number of students:")
        self.collect_scores_button = ttk.Button(self.root, text="Collect Scores", command=self.collect_scores)
        self.results_text = tk.Text(self.root, state="disabled", wrap="word")

    def collect_scores(self):
        try:
            students = int(self.students_entry.get())
            for i in range(students):
                score = simpledialog.askinteger(f"Student {i + 1} Score", f"Enter score for student {i + 1}:")
                while score is None:
                    score = simpledialog.askinteger(f"Student {i + 1} Score", f"Enter score for student {i + 1}:")

                self.student_grader.add_student(score)

            results = self.student_grader.calculate_grades()

            self.display_results(results)

        except ValueError:
            messagebox.showerror("Error", "Please enter valid scores for each student.")

    def display_results(self, results):
        self.results_text.config(state="normal")
        self.results_text.delete(1.0, tk.END)
        for result in results:
            self.results_text.insert(tk.END, f"Score: {result[0]}, Grade: {result[1]}\n")
        self.results_text.config(state="disabled")

    def run(self):
        self.students_label.pack()
        self.students_entry.pack()
        self.collect_scores_button.pack()
        self.results_text.pack()
        self.root.mainloop()
