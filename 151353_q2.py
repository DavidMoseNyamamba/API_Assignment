#Create a Student class with attributes name and grades 
# (a dictionary with subjects as keys and grades as values).
class Student:
# __init__(self, name): Initializes a student with a name and an empty dictionary for grades.
    def __init__(self, name):
        self.name = name
        self.grades = {}
  # add_grade(self, subject, grade): Adds a grade for a specific subject.
    def add_grade(self, subject, grade):
        self.grades[subject] = grade

# get_average_grade(self): Calculates and returns the average grade for the student.

    def get_average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades.values()) / len(self.grades)
    

#__init__(self): Initializes an empty list of students.
class Classroom:
    def __init__(self):
        self.students = []

#add_student(self, student): Adds a student to the classroom.
    def add_student(self, student):
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

#display_students(self): Displays all students and their grades.
    def display_students(self):
        if not self.students:
            print("No students in the class.")
        else:
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

#get_student_average(self, student_name): Prints the average grade for a specific student by name.
    def get_student_average(self, student_name):
        for student in self.students:
            if student.name.lower() == student_name.lower():
                average = student.get_average_grade()
                print(f"Average grade for {student.name}: {average:.2f}")
                return
        print(f"Student {student_name} not found.")
#get_class_average_for_subject(self, subject): Prints the class average for a specific subject.
    def get_class_average_for_subject(self, subject):
        total = 0
        count = 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades recorded for subject: {subject}")
        else:
            average = total / count
            print(f"Class average for {subject}: {average:.2f}")

# Demonstrating the functionality
#using main() function:
#Provides a simple command-line interface for interacting with the Classroom and Student classes.
#Allows adding students,
#  adding grades, 
# displaying students,
#  getting individual student averages, 
# and getting class averages for subjects.
def main():
    classroom = Classroom()
    
    while True:
        print("\nClassroom Management System")
        print("1. Add a new student")
        print("2. Add grade for a student")
        print("3. Display all students")
        print("4. Get average grade of a student")
        print("5. Get class average for a subject")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter student name: ")
            student = Student(name)
            classroom.add_student(student)
        elif choice == '2':
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = float(input("Enter grade: "))
            for student in classroom.students:
                if student.name.lower() == name.lower():
                    student.add_grade(subject, grade)
                    print(f"Grade {grade} added for {subject} to student {name}.")
                    break
            else:
                print(f"Student {name} not found.")
        elif choice == '3':
            classroom.display_students()
        elif choice == '4':
            name = input("Enter student name: ")
            classroom.get_student_average(name)
        elif choice == '5':
            subject = input("Enter subject: ")
            classroom.get_class_average_for_subject(subject)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
