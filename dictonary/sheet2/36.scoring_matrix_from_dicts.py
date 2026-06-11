def scoring_matrix_from_dicts(students: list[str], subjects: list[str], scores: list[list[int]]) -> dict[str, dict[str, int]]:
    return {student: {subject: scores[row][col] for col, subject in enumerate(subjects)} for row, student in enumerate(students)}

result = scoring_matrix_from_dicts(['A', 'B'], ['math', 'sci'], [[90, 80], [85, 95]])
