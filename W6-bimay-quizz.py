
lecturers = []  

def add_lecturer(name, id):
    lecturer = {
        "id": id,
        "name": name
    }
    lecturers.append(lecturer)


classes = []  
def create_class(class_id, class_name, lecturer_id):
    course = {
        "class_id": class_id,
        "class_name": class_name,
        "lecturer_id": lecturer_id,
        "students": []
    }
    classes.append(course)


def add_student_to_class(class_id, student_name):
    for course in classes:
        if course["class_id"] == class_id:
            course["students"].append(student_name)
            break


def show_system():
    print("Lecturers:")
    for lecturer in lecturers:
        print(f"ID: {lecturer['id']}, Name: {lecturer['name']}")
    
    print("\nClasses:")
    for course in classes:
        print(f"Class ID: {course['class_id']}, Class Name: {course['class_name']}, Lecturer ID: {course['lecturer_id']}")
        print("Students Enrolled:", ', '.join(course["students"]))

# Example
# Add lecturers
add_lecturer("Dr. Zandos", "001")
add_lecturer("Prof. Sanny", "002")

# Create classes
create_class("C001", "Algorithm And Prorgramming", "001")
create_class("C002", "Turing Computing", "002")

# add student tto class
add_student_to_class("C001", "Zandos zee")
add_student_to_class("C001", "William Xen")
add_student_to_class("C002", "Chenny Chan")


show_system()