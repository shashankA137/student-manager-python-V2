import json
import os
from student import Student

FILE_NAME = "students.json"


# ---------- FILE HANDLING ----------

def load_students():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            return [Student.from_dict(s) for s in data]
    except:
        return []


def save_students(students):
    with open(FILE_NAME, "w") as f:
        json.dump([s.to_dict() for s in students], f, indent=4)


# ---------- OPERATIONS ----------

def add_student(students):
    roll = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()
    course = input("Enter student course: ").strip()

    if not roll or not name or not course:
        print("Fields cannot be empty")
        return

    for s in students:
        if s.roll == roll:
            print("Roll number already exists")
            return

    students.append(Student(roll, name, course))
    save_students(students)
    print("Student added successfully")


def view_students(students):
    if not students:
        print("No records found")
        return

    students.sort(key=lambda x: x.roll)

    print("\nStudent List")
    for s in students:
        print("Roll:", s.roll, "| Name:", s.name, "| Course:", s.course)

    print("Total students:", len(students))


def search_student(students):
    roll = input("Enter roll number to search: ").strip()

    for s in students:
        if s.roll == roll:
            print("Student found")
            print("Roll:", s.roll, "Name:", s.name, "Course:", s.course)
            return

    print("Student not found")


def update_student(students):
    roll = input("Enter roll number to update: ").strip()

    for s in students:
        if s.roll == roll:
            new_name = input("Enter new name: ").strip()
            new_course = input("Enter new course: ").strip()

            if new_name:
                s.name = new_name
            if new_course:
                s.course = new_course

            save_students(students)
            print("Student updated")
            return

    print("Student not found")


def delete_student(students):
    roll = input("Enter roll number to delete: ").strip()

    for s in students:
        if s.roll == roll:
            confirm = input("Are you sure? (y/n): ").lower()
            if confirm == "y":
                students.remove(s)
                save_students(students)
                print("Student deleted")
            else:
                print("Delete cancelled")
            return

    print("Student not found")


# ---------- MENU ----------

def menu():
    students = load_students()

    while True:
        print("\n===== STUDENT MANAGER =====")
        print("1. Add student")
        print("2. View students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        choice = input("Enter option: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            view_students(students)

        elif choice == "3":
            search_student(students)

        elif choice == "4":
            update_student(students)

        elif choice == "5":
            delete_student(students)

        elif choice == "6":
            print("Program closed")
            break

        else:
            print("Invalid choice")


# ---------- START ----------

if __name__ == "__main__":
    menu()
