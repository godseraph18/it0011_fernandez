def load_file(filename):
    records = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                if len(parts) == 4:
                    student_id = parts[0]
                    first_name, last_name = parts[1].split(',')
                    class_standing = float(parts[2])
                    major_exam = float(parts[3])
                    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    except FileNotFoundError:
        pass
    return records

def save_file(filename, records):
    with open(filename, 'w') as file:
        for record in records:
            student_id, (first_name, last_name), class_standing, major_exam = record
            file.write(f"{student_id}|{first_name},{last_name}|{class_standing}|{major_exam}\n")

def calculate_grade(class_standing, major_exam):
    return round((class_standing * 0.6) + (major_exam * 0.4), 2)

def display_records(records):
    print("\nStudent Records:")
    for record in records:
        student_id, (first_name, last_name), class_standing, major_exam = record
        final_grade = calculate_grade(class_standing, major_exam)
        print(f"ID: {student_id}, Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam: {major_exam}, Final Grade: {final_grade}")

def add_record(records):
    student_id = input("Enter 6-digit Student ID: ")
    if len(student_id) != 6 or not student_id.isdigit():
        print("Invalid ID. Must be a 6-digit number.")
        return
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = float(input("Enter Class Standing Grade: "))
    major_exam = float(input("Enter Major Exam Grade: "))
    records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record(records):
    student_id = input("Enter Student ID to edit: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            first_name = input("Enter New First Name: ")
            last_name = input("Enter New Last Name: ")
            class_standing = float(input("Enter New Class Standing Grade: "))
            major_exam = float(input("Enter New Major Exam Grade: "))
            records[i] = (student_id, (first_name, last_name), class_standing, major_exam)
            print("Record updated successfully.")
            return
    print("Record not found.")

def delete_record(records):
    student_id = input("Enter Student ID to delete: ")
    for i, record in enumerate(records):
        if record[0] == student_id:
            del records[i]
            print("Record deleted successfully.")
            return
    print("Record not found.")

def order_by_lastname(records):
    return sorted(records, key=lambda x: x[1][1])

def order_by_grade(records):
    return sorted(records, key=lambda x: calculate_grade(x[2], x[3]), reverse=True)

def show_student_record(records):
    student_id = input("Enter Student ID to search: ")
    for record in records:
        if record[0] == student_id:
            student_id, (first_name, last_name), class_standing, major_exam = record
            final_grade = calculate_grade(class_standing, major_exam)
            print(f"ID: {student_id}, Name: {first_name} {last_name}, Class Standing: {class_standing}, Major Exam: {major_exam}, Final Grade: {final_grade}")
            return
    print("Record not found.")

def main():
    filename = "students.txt"
    records = load_file(filename)
    
    while True:
        print("\nRecord Management Menu:")
        print("1. Show All Students Record")
        print("2. Order by Last Name")
        print("3. Order by Grade")
        print("4. Show Student Record")
        print("5. Add Record")
        print("6. Edit Record")
        print("7. Delete Record")
        print("8. Save File")
        print("9. Save As File")
        print("10. Open File")
        print("11. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_records(records)
        elif choice == "2":
            display_records(order_by_lastname(records))
        elif choice == "3":
            display_records(order_by_grade(records))
        elif choice == "4":
            show_student_record(records)
        elif choice == "5":
            add_record(records)
        elif choice == "6":
            edit_record(records)
        elif choice == "7":
            delete_record(records)
        elif choice == "8":
            save_file(filename, records)
            print("File saved successfully.")
        elif choice == "9":
            new_filename = input("Enter new filename: ")
            save_file(new_filename, records)
            print("File saved successfully as", new_filename)
        elif choice == "10":
            filename = input("Enter filename to open: ")
            records = load_file(filename)
            print("File loaded successfully.")
        elif choice == "11":
            print("Exiting program.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
