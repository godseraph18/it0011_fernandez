def save_student_info():
    last_name = input("Enter last name: ")
    first_name = input("Enter first name: ")
    age = input("Enter age: ")
    contact = input("Enter contact number: ")
    course = input("Enter course: ")

    student_info = f"Last Name: {last_name}\nFirst Name: {first_name}\nAge: {age}\nContact Number: {contact}\nCourse: {course}\n\n"

    with open("students.txt", "a") as file:
        file.write(student_info)

    print("Student information saved to 'students.txt'.")

save_student_info()