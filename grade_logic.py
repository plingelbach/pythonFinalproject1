def get_grade(score, best_score):
    if score >= best_score - 10:
        return "A"
    elif score >= best_score - 20:
        return "B"
    elif score >= best_score - 30:
        return "C"
    elif score >= best_score - 40:
        return "D"
    else:
        return "F"
