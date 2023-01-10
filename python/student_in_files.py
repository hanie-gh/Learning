def write_info(file_name):
    text_file = open(file_name, "w")
    while input("Do you want to enter information for a student? (Y or N): ") in ("Y", "y"):
        text_file.write(input("Enter First Name: ")+',')
        text_file.write(input("Enter Last Name: ")+',')
        text_file.write(input("Enter Student.ID: ")+',')
        id_pass = input("Enter ID: ")
        text_file.write(id_pass+',')
        text_file.write(id_pass+'\n')
    print("The information for the students has been saved!")

def read_info(file_name):
    text_file = open(file_name, "r")
    for line in text_file:
        student_info = line.split(',')
        print("First Name: " + student_info[0])
        print("Last Name: " + student_info[1])
        print("Student.ID: " + student_info[2])
        print("ID: " + student_info[3])

def change_pass(file_name, stu_id, new_pass):
    text_file = open(file_name, 'r')
    lines = ""
    for line in text_file:
        student_info = line.split(',')
        if student_info[2] == stu_id:
           line = student_info[0]+','+student_info[1]+','+student_info[2]+','+student_info[3]+','+new_pass+'\n'
        lines += line
    text_file = open(file_name, 'w')
    text_file.write(lines)

def remove_info(file_name, stu_id):
    text_file = open(file_name, 'r')
    lines = ""
    for line in text_file:
        student_info = line.split(',')
        if student_info[2] != stu_id:
            lines += line
    text_file = open(file_name, 'w')
    text_file.write(lines)

if __name__ == '__main__':
    file_name = 'students.txt'
    ##########################################################################
    write_info(file_name)
    ##########################################################################
    print("\nShowing the information of a students: ")
    read_info(file_name)
    ##########################################################################
    print("Remove the information for a student")
    stu_id = input("Enter the student id: ")
    remove_info(file_name, stu_id)
    print(f'The information for student with st.id {stu_id}, has been removed!')
    ##########################################################################
    print("Change the password for a student")
    stu_id = input("Enter the student id: ")
    new_pass = input("Enter the new pass: ")
    change_pass(file_name, stu_id, new_pass)
    print(f'The new password for student with st.id {stu_id}, has been changed!')
    ##########################################################################

