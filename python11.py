def calculate_avg(m1, m2, m3):
    average = (m1 + m2 + m3) / 3
    return average


def is_pass(average):
    return average >= 50


def grade(average):
    if average >= 80:
        return "A"
    elif average >= 60:
        return "B"
    elif average >= 50:
        return "C"
    else:
        return "F"


def Student_report(name, m1, m2, m3):
    average = calculate_avg(m1, m2, m3)

    print("Name:", name)
    print("Average:", average)
    is_pass(average)

    
    print("Grade:", grade(average))


name = input("Enter Student Name: ")
m1 = int(input("Enter Marks of Subject 1: "))
m2 = int(input("Enter Marks of Subject 2: "))
m3 = int(input("Enter Marks of Subject 3: "))

Student_report(name, m1, m2, m3)