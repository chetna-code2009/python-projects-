students=[]

def add_student():
    name=input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    try:
        age=int(input("Enter student age: "))
    except ValueError:
        print("Age must be a valid integer.")
        return
    if  age <= 0:
        print("Age must be a positive integer.")
        return
    try:
        roll_number=int(input("Enter student roll number: "))
    except ValueError:
        print("Roll number must be a valid integer.")
        return
    if not roll_number or roll_number <= 0:
        print("Roll number must be a positive integer.")
        return
    for student in students:
        if student["roll_number"]==roll_number:
            print("roll number already exists.please enter a unique roll number. ")
            return
    student={'name':name,'age':age,'roll_number':roll_number}
    students.append(student) 
    print("Student added successfully➕ψ(｀∇´)ψ")  

def view_students():
    if not students:
        print("No students found.")
        return

    print("List of students^_^")

    for student in students:
        print(
            f"Name: {student['name']}, "
            f"Age: {student['age']}, "
            f"Roll Number: {student['roll_number']}"
        )

def search_student():
    try:
        roll_number = int(input("Enter student roll number to search: "))
    except ValueError:
        print("Roll number must be a valid integer.")
        return

    if roll_number <= 0:
        print("Roll number must be a positive integer.")
        return

    for student in students:
        if student["roll_number"] == roll_number:
            print(
                f"Student found: Name: {student['name']}, "
                f"Age: {student['age']}, "
                f"Roll Number: {student['roll_number']}"
            )
            return

    print("Student not found.")

    

def delete_student():
    try:
        roll_number = int(input("Enter student roll number to delete: "))
    except ValueError:
        print("Roll number must be a valid integer.")
        return

    if roll_number <= 0:
        print("Roll number must be a positive integer.")
        return

    for i, student in enumerate(students):
        if student["roll_number"] == roll_number:
            del students[i]
            print("Student deleted successfully.✔✔")
            return

    print("Student not found.")


def update_student():
    print("\n✏️ Update Student")

    try:
        roll_number = int(input("Enter student roll number to update: "))
    except ValueError:
        print("❌ Roll number must be a valid integer.")
        return

    if roll_number <= 0:
        print("❌ Roll number must be a positive integer.")
        return

    for student in students:
        if student["roll_number"] == roll_number:

            name = input(
                "Enter new student name "
                "(leave blank to keep current): "
            ).strip()

            age_input = input(
                "Enter new student age "
                "(leave blank to keep current): "
            ).strip()

            if name:
                student["name"] = name

            if age_input:
                try:
                    age = int(age_input)
                except ValueError:
                    print("❌ Age must be a valid integer.")
                    return

                if age <= 0:
                    print("❌ Age must be a positive integer.")
                    return

                student["age"] = age

            print("✅ Student updated successfully.")
            return

    print("❌ Student not found.")
 

def main():
    while True:
        print("\n📚 Student Management System")
        print("1. ➕ Add Student")
        print("2. 👀 View Students")
        print("3. 🔍 Search Student")
        print("4. 🗑️ Delete Student")
        print("5. ✏️ Update Student")
        print("6. 🚪 Exit")

        choice = input("👉 Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            update_student()
        elif choice == "6":
            print("👋 Exiting the program.")
            break
        else:
            print("❌ Invalid choice. Please enter a number from 1 to 6.")


main()        





    


        

                    
