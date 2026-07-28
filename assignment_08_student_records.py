
def display_menu():
    print("================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")
 
 
def calculate_average(scores):
    """Return the average of `scores`, rounded to 2 decimal places."""
    return round(sum(scores) / len(scores), 2)
 
 
def find_student(students, student_id):
    """Return the student dict with the matching ID, or None if not found."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None
 
 
def add_student(students):
    """Prompt for a new student's details and append the record to `students`."""
    name = input("Student name: ")
    student_id = int(input("Student ID: "))
 
    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(1, num_scores + 1):
        score = float(input(f"Enter score {i}: "))
        scores.append(score)
 
    students.append({"name": name, "id": student_id, "scores": scores})
    print(f'Student "{name}" added successfully.')
 
 
def display_students(students):
    """Print a formatted table of every student's name, ID, scores, and average."""
    if not students:
        print("No students have been added yet.")
        return
 
    separator = "-" * 50
    print(separator)
    print(f"{'Name':<15}{'ID':<12}{'Scores':<15}{'Average'}")
    print(separator)
 
    for student in students:
        scores_str = ", ".join(str(int(s)) if s == int(s) else str(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f"{student['name']:<15}{student['id']:<12}{scores_str:<15}{average}")
 
    print(separator)
 
 
def show_student_average(students):
    """Prompt for a student ID and print that student's average score."""
    student_id = int(input("Enter student ID: "))
    student = find_student(students, student_id)
 
    if student is None:
        print(f"Error: No student found with ID {student_id}.")
        return
 
    average = calculate_average(student["scores"])
    print(f"{student['name']}'s average score: {average}")
 
 
def main():
    students = []
 
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        print()
 
        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            show_student_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number from 1 to 4.")
 
        print()
 
 
if __name__ == "__main__":
    main()