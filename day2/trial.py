class Student:

    def __init__(self, name, age, marks):

        self.name = name

        self.age = age

        self.marks = marks

    def to_dict(self):

        return {

            "Name": self.name,

            "Age": self.age,

            "Marks": self.marks

        }

students = {}         # {student_id: Student object}

student_id = 1        # Unique ID for each student

while True:

    print("\n--- Student Record Menu ---")

    print("1. Add Student")

    print("2. View Students")

    print("3. Update Student")

    print("4. Delete Student")

    print("5. Exit")

    try:

        choice = int(input("Enter your choice: "))

        if choice == 1:

            name = input("Enter name: ")

            age = int(input("Enter age: "))

            marks = int(input("Enter marks: "))

            students[student_id] = Student(name, age, marks)

            print(f"Student added with ID: {student_id}")

            student_id += 1

        elif choice == 2:

            if not students:

                print("No student records found.")

            else:

                print("\n--- All Students (as dicts) ---")

                for sid, student in students.items():

                    student_data = student.to_dict()

                    print(f"{sid}: {student_data}")

        elif choice == 3:

            sid = int(input("Enter Student ID to update: "))

            if sid in students:

                name = input("New name: ")

                age = int(input("New age: "))

                marks = int(input("New marks: "))

                students[sid] = Student(name, age, marks)

                print("Student record updated.")

            else:

                print("Student ID not found.")

        elif choice == 4:

            sid = int(input("Enter Student ID to delete: "))

            if sid in students:

                del students[sid]

                print("Student record deleted.")

            else:

                print("Student ID not found.")

        elif choice == 5:

            print("Exiting program.")

            break

        else:

            print("Invalid choice. Please enter a number between 1 and 5.")

    except ValueError:

        print("Invalid input. Please enter a valid number.")
 