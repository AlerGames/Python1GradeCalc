#declare and initialize the variable which stores the total grade
total_grade: float = 0.0

#takes in the amount of completed assignments, assignments assigned and the weight of them all 
def add_grade_by_completed_assignments(weight: float, assignments_assigned: int, text: str):
    global total_grade
    total_grade += ((int(input(text)) / assignments_assigned)) * weight 

#takes in the weight of an exam and the score
def add_grade_by_exam(weight:float, text:str):
    global total_grade
    total_grade += (weight * float(input(text))) / 100

#prompt and assign values to the different grades
add_grade_by_completed_assignments(20.0, 6, "Enter the number of labs completed: ")
add_grade_by_completed_assignments(15.0, 6, "Enter the number of quizzes completed: ")
add_grade_by_exam(4.0, "Enter grade for Assignment 1: ")
add_grade_by_exam(4.0, "Enter grade for Assignment 2: ")
add_grade_by_exam(4.0, "Enter grade for Assignment 3: ")
add_grade_by_exam(4.0, "Enter grade for Assignment 4: ")
add_grade_by_exam(12.5, "Enter grade for Midterm 1: ")
add_grade_by_exam(12.5, "Enter grade for Midterm 2: ")
add_grade_by_exam(18.0, "Enter grade for Final Exam: ")
add_grade_by_exam(6.0, "Enter grade for Midterms and Final Preparation: ")

#display final grade
print("Your grade is: %s" %(round(total_grade)))
