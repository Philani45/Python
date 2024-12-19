class EmptyRosterError(Exception):
    pass

class Student:
    def __init__(self, first, last, gpa):
        self.first = first
        self.last = last
        self.gpa = gpa

    def get_gpa(self):
        return self.gpa

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

class Course:
    def __init__(self):
        self.roster = []

    def add_student(self, student):
        self.roster.append(student)

    def course_size(self):
        return len(self.roster)

    def find_student_highest_gpa(self):
        if not self.roster:
            raise EmptyRosterError('Exception: Course Roster is Empty')
        return max(self.roster, key=lambda student: student.get_gpa())

# Example usage:
course = Course()

while True:
    try:
        first = input("Enter student's first name (or 'stop' to finish): ")
        if first.lower() == 'stop':
            break
        last = input("Enter student's last name: ")
        gpa = float(input("Enter student's GPA: "))
        student = Student(first, last, gpa)
        course.add_student(student)
    except ValueError:
        print("Error: Please enter a valid numeric GPA.")

size = course.course_size()
if size > 0:
    highest_gpa_student = course.find_student_highest_gpa()
    print(f"\nNumber of students enrolled: {size}")
    print(f"Highest GPA Student: {highest_gpa_student.get_first()} {highest_gpa_student.get_last()} with GPA {highest_gpa_student.get_gpa()}")
