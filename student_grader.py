from student import Student


class StudentGrader:
    def __init__(self):
        self.students = []

    def add_student(self, score):
        student = Student(score)
        self.students.append(student)

    def get_best_score(self):
        if not self.students:
            return None
        return max(student.score for student in self.students)

    def calculate_grades(self):
        best_score = self.get_best_score()
        if best_score is None:
            return []

        results = [(student.score, student.grade(best_score)) for student in self.students]
        return results
