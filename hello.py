class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"\nID      : {self.student_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(sid, name, age, course)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n------ Student List ------")
        for student in self.students:
            student.display()

    def search_student(self):
        sid = input("Enter Student ID to search: ")

        for student in self.students:
            if student.student_id == sid:
                print("\nStudent Found")
                student.display()
                return

        print("Student not found.")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")

        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()



    print("Second commit")

    def update_student(self):
    sid = input("Enter Student ID to update: ")

    for student in self.students:
        if student.student_id == sid:
            print("Leave blank to keep the current value.")

            new_name = input(f"Name ({student.name}): ")
            new_age = input(f"Age ({student.age}): ")
            new_course = input(f"Course ({student.course}): ")

            if new_name:
                student.name = new_name
            if new_age:
                student.age = new_age
            if new_course:
                student.course = new_course

            print("Student updated successfully!")
            return

    print("Student not found.")


    class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"\nID      : {self.student_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(sid, name, age, course)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n------ Student List ------")
        for student in self.students:
            student.display()

    def search_student(self):
        sid = input("Enter Student ID to search: ")

        for student in self.students:
            if student.student_id == sid:
                print("\nStudent Found")
                student.display()
                return

        print("Student not found.")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")

        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()



    print("Second commit")

    def update_student(self):
    sid = input("Enter Student ID to update: ")

    for student in self.students:
        if student.student_id == sid:
            print("Leave blank to keep the current value.")

            new_name = input(f"Name ({student.name}): ")
            new_age = input(f"Age ({student.age}): ")
            new_course = input(f"Course ({student.course}): ")

            if new_name:
                student.name = new_name
            if new_age:
                student.age = new_age
            if new_course:
                student.course = new_course

            print("Student updated successfully!")
            return

    print("Student not found.")


class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"\nID      : {self.student_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(sid, name, age, course)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n------ Student List ------")
        for student in self.students:
            student.display()

    def search_student(self):
        sid = input("Enter Student ID to search: ")

        for student in self.students:
            if student.student_id == sid:
                print("\nStudent Found")
                student.display()
                return

        print("Student not found.")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")

        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()



    print("Second commit")

    def update_student(self):
    sid = input("Enter Student ID to update: ")

    for student in self.students:
        if student.student_id == sid:
            print("Leave blank to keep the current value.")

            new_name = input(f"Name ({student.name}): ")
            new_age = input(f"Age ({student.age}): ")
            new_course = input(f"Course ({student.course}): ")

            if new_name:
                student.name = new_name
            if new_age:
                student.age = new_age
            if new_course:
                student.course = new_course

            print("Student updated successfully!")
            return

    print("Student not found.")


class Student:
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print(f"\nID      : {self.student_id}")
        print(f"Name    : {self.name}")
        print(f"Age     : {self.age}")
        print(f"Course  : {self.course}")


class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self):
        sid = input("Enter Student ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        course = input("Enter Course: ")

        student = Student(sid, name, age, course)
        self.students.append(student)
        print("Student added successfully!")

    def view_students(self):
        if not self.students:
            print("No students available.")
            return

        print("\n------ Student List ------")
        for student in self.students:
            student.display()

    def search_student(self):
        sid = input("Enter Student ID to search: ")

        for student in self.students:
            if student.student_id == sid:
                print("\nStudent Found")
                student.display()
                return

        print("Student not found.")

    def delete_student(self):
        sid = input("Enter Student ID to delete: ")

        for student in self.students:
            if student.student_id == sid:
                self.students.remove(student)
                print("Student deleted successfully.")
                return

        print("Student not found.")


def main():
    manager = StudentManager()

    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            manager.add_student()
        elif choice == "2":
            manager.view_students()
        elif choice == "3":
            manager.search_student()
        elif choice == "4":
            manager.delete_student()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()



    print("Second commit")

    def update_student(self):
    sid = input("Enter Student ID to update: ")

    for student in self.students:
        if student.student_id == sid:
            print("Leave blank to keep the current value.")

            new_name = input(f"Name ({student.name}): ")
            new_age = input(f"Age ({student.age}): ")
            new_course = input(f"Course ({student.course}): ")




def sort_students(self):
    if not self.students:
        print("No students available.")
        return

    self.students.sort(key=lambda student: student.name.lower())
    


    


