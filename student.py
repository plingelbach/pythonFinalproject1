class Student:
    def __init__(self, score):
        self.score = score

    def grade(self, best_score):
        if self.score >= best_score - 10:
            return "A"
        elif self.score >= best_score - 20:
            return "B"
        elif self.score >= best_score - 30:
            return "C"
        elif self.score >= best_score - 40:
            return "D"
        else:
            return "F"
