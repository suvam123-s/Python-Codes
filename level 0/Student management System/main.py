import os

class Student:
    def _init_(self, id, name, eca, grades, password):
        self.id = id
        self.name = name
        self.eca = eca
        self.grades = grades
        self.password = password

def create_files_if_not_exist(users_file, eca_file, grades_file, passwords_file):
    # Check if files exist, if not, create them
    files = [users_file, eca_file, grades_file, passwords_file]
    for file in files:
        if not os.path.exists(file):
            with open(file, 'w') as f:
                f.write("")  # Just create an empty file if it doesn't exist
def add_student(users_file, eca_file, grades_file, passwords_file):
    try:
        id = input("Enter the ID of the student: ")
        name = input("Enter the name of the student: ")
        eca = input("Enter the ECA done: ")
        grades = input("Enter the grades received: ")
        username = input("Set the username: ")  # Prompt for username
        password = input("Set the password: ")  # Prompt for password

        # Attempt to convert ID to integer within the try block
        id = int(id)

        # Write student information to respective files
        with open(users_file, 'a') as file:
            file.write(f"{id},{name}\n")

        with open(eca_file, 'a') as file:
            file.write(f"{id},{name},{eca}\n")

        with open(grades_file, 'a') as file:
            file.write(f"{id},{name},{grades}\n")

        with open(passwords_file, 'a') as file:
            file.write(f"{id},{username},{password}\n")  # Write username and password to passwords file

        print("Student added successfully!")   
    except Exception as e:
        print(f"An error occurred: {e}")



def modify_student(users_file, eca_file, grades_file, passwords_file):
    try:
        id = input("Enter the ID of the student to modify: ")

        # Modify user information
        with open(users_file, 'r') as file:
            lines = file.readlines()

        with open(users_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] == id:
                    name = input("Enter the new name: ")
                    file.write(f"{id},{name}\n")
                else:
                    file.write(line)

        # Modify ECA
        with open(eca_file, 'r') as file:
            lines = file.readlines()

        with open(eca_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] == id:
                    eca = input("Enter the new ECA: ")
                    file.write(f"{id},{parts[1]},{eca}\n")
                else:
                    file.write(line)

        # Modify Grades
        with open(grades_file, 'r') as file:
            lines = file.readlines()

        with open(grades_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] == id:
                    grades = input("Enter the new grades: ")
                    file.write(f"{id},{parts[1]},{grades}\n")
                else:
                    file.write(line)

        # Modify Passwords
        with open(passwords_file, 'r') as file:
            lines = file.readlines()

        with open(passwords_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] == id:
                    password = input("Enter the new password: ")
                    file.write(f"{id},{parts[1]},{password}\n")
                else:
                    file.write(line)

        print("Student information modified successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def delete_student(users_file, eca_file, grades_file, passwords_file):
    try:
        id = input("Enter the ID of the student to delete: ")

        # Delete from users_file
        with open(users_file, 'r') as file:
            lines = file.readlines()

        with open(users_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] != id:
                    file.write(f"{line}\n")

        # Delete from eca_file
        with open(eca_file, 'r') as file:
            lines = file.readlines()

        with open(eca_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] != id:
                    file.write(f"{line}\n")

        # Delete from grades_file
        with open(grades_file, 'r') as file:
            lines = file.readlines()

        with open(grades_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] != id:
                    file.write(f"{line}\n")

        # Delete from passwords_file
        with open(passwords_file, 'r') as file:
            lines = file.readlines()

        with open(passwords_file, 'w') as file:
            for line in lines:
                parts = line.strip().split(',')
                if parts[0] != id:
                    file.write(f"{line}\n")

        print("Student deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_student(name, users_file, eca_file, grades_file, passwords_file):
    try:
        id = input("Enter the ID of the student: ")

        with open(users_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == id and parts[1] == name:
                    print("Student information:")
                    print(f"ID: {parts[0]}")
                    print(f"Name: {parts[1]}")

        with open(eca_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == id and parts[1] == name:
                    print(f"ECA Done: {parts[2]}")

        with open(grades_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == id and parts[1] == name:
                    print(f"Grades Received: {parts[2]}")
    except Exception as e:
        print(f"An error occurred: {e}")

def student_menu(name, users_file, eca_file, grades_file):
    try:
        while True:
            print("\nStudent Menu:")
            print("1. List ECA")
            print("2. List Grades")
            print("3. Logout")
            option = int(input("Enter your option: "))

            if option == 1:
                view_eca(name, users_file, eca_file)
            elif option == 2:
                view_grades(name, users_file, grades_file)
            elif option == 3:
                print("Logging out from student account.")
                break
            else:
                print("Invalid option. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_eca(name, users_file, eca_file):
    try:
        id = input("Enter the ID of the student: ")

        with open(users_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == id:
                    print("Student information:")
                    print(f"ID: {parts[0]}")
                    print(f"Name: {parts[1]}")

        with open(eca_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == id:
                    print(f"ECA Done: {parts[2]}")
    except Exception as e:
        print(f"An error occurred: {e}")

def view_grades(name, users_file, grades_file):
    try:
        id = input("Enter your ID: ")

        with open(users_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == id and parts[1] == name:
                    print("Student information:")
                    print(f"ID: {parts[0]}")
                    print(f"Name: {parts[1]}")

        with open(grades_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[0] == id and parts[1] == name:
                    print(f"Grades Received: {parts[2]}")
                    return

        print("No grades found for the given ID and name.")
    except Exception as e:
        print(f"An error occurred: {e}")

def student_login(users_file, eca_file, grades_file, passwords_file):
    try:
        username = input("shubham: ")
        password = input("password: ")

        with open(passwords_file, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    print("Skipping invalid line in passwords file.")
                    continue
                if parts[1] == username and parts[2] == password:
                    print("Student login successful!")
                    student_menu(username, users_file, eca_file, grades_file)
                    return True
        print("Student login failed. Please try again.")
        return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def admin_menu(users_file, eca_file, grades_file, passwords_file):
    try:
        while True:
            print("\nAdmin Menu:")
            print("1. New student")
            print("2. modify student")
            print("3. List student")
            print("4. Logout")
            print("5. Delete student")
            option = int(input("Enter your option: "))
            
            if option == 1:
                add_student(users_file, eca_file, grades_file, passwords_file)
            elif option == 2:
                modify_student(users_file, eca_file, grades_file, passwords_file)
            elif option == 3:
                name = input("Enter the name of the student: ")
                view_student(name, users_file, eca_file, grades_file, passwords_file)  # Added name argument
            elif option == 4:
                print("Logging out from admin account.")
                break
            elif option == 5:
                delete_student(users_file, eca_file, grades_file, passwords_file)
            else:
                print("Invalid option. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

def admin_login():
    try:
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username == "admin" and password == "password":
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def main():
    try:
        users_file = 'users.txt'
        eca_file = 'eca.txt'
        grades_file = 'grades.txt'
        passwords_file = 'passwords.txt'
        
        # Create files if they don't exist
        create_files_if_not_exist(users_file, eca_file, grades_file, passwords_file)
        
        while True:
            print("Welcome to the main home screen!")
            print("1. Login as Admin")
            print("2. Login as Student")
            print("3. Exit")
            option = int(input("Enter your option: "))
            
            if option == 1:
                if admin_login():
                    print("Admin login successful!")
                    admin_menu(users_file, eca_file, grades_file, passwords_file)
                else:
                    print("Admin login failed. Please try again.")
            elif option == 2:
                student_login(users_file, eca_file, grades_file, passwords_file)
            elif option == 3:
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    main()