import json

try:
    with open("project1.json","r") as file:
        students = json.load(file)
except (FileNotFoundError, json.JSONDecodeError):
    print("Created a new list, there was nothing before")
    students = []

while True:
    print("\n1. Add student")
    print("2. Show students")
    print("3. Search student")
    print("4. Delete student")
    print("5. To change Age")
    print("6. Exit")

    enter = int(input("Enter the option: "))

    if enter == 1:
        enter_name = input("Enter the name: ")
        enter_age = int(input("Enter the age: "))
        student = {"name": enter_name, "age": enter_age}
        students.append(student)

        with open("project1.json","w") as file:
            json.dump(students,file,indent=4)

    elif enter == 2:
        if not students:
            print("No registered students")
        else:
            for s in students:
                print(s["name"], "-", s["age"])

    elif enter == 3:
        name = input("Enter student name: ")
        found = False

        for s in students:
            if name.lower() == s["name"].lower():
                print(s["name"], "-", s["age"])
                found = True
                break

        if not found:
            print("No such student exists")

    elif enter == 4:
        name = input("Enter student name to delete: ")
        removed = False

        for s in students:
            if name.lower() == s["name"].lower():
                students.remove(s)
                print("Student removed")
                removed = True
                break

        if not removed:
            print("No student found")

        with open("project1.json","w") as file:
            json.dump(students,file,indent=4)
    elif enter ==5:
        name=input("Enter student name:")
        found= False
        for s in students:
            if name.lower()== s["name"].lower():
                new_age=int(input("Enter new age:"))
                s["age"]= new_age
                found = True
                print("Age updated")
                break
        if not found:
            print("No student found")
        with open("project1.json","w") as file:
            json.dump(students,file, indent=4)

    elif enter == 6:
        print("Thank you, goodbye")
        break

    else:
        print("Invalid input, please type between 1–5")
    
    