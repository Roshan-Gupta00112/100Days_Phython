student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

for st_name in student_scores:
    print(f"The score of the {st_name} is: {student_scores[st_name]}")

student_grades = dict()

for st_nam in student_scores:
    prs_stu_score = student_scores[st_nam]
    if prs_stu_score > 90:
        student_grades[st_nam] = "Outstanding"
    elif prs_stu_score > 80:
        student_grades[st_nam] = "Exceeds Expectations"
    elif prs_stu_score > 70:
        student_grades[st_nam] = "Acceptable"
    else:
        student_grades[st_nam] = "Fail"

for st_name in student_grades:
    print(f"The grade of {st_name} is: {student_grades[st_name]}.")


student_scores[1] = 0
for st_name in student_scores:
    print(f"Student name and score after modifying student_scores dictionary is, {st_name}: {student_scores[st_name]}")