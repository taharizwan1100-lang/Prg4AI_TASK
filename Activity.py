def calculate_avg(m1,m2,m3):
    average=(m1+m2+m3)/3
    return average
def is_pass(average):
    return average>=50
def grade(average):
    if avg>=80:
        msg= "Grade is A"
    elif avg>=60:
        msg= "Grade is B"
    elif avg>50:
        msg= "Grade is c"
    else:
        msg = "Fail"
    return msg
def Student_report(name,m1,m2,m3):

     print("Name:", name)
        print("Average:", average)
    
        if is_pass(average):
            print("Result: Pass")
        else:
            print("Result: Fail")
    
        print("Grade:", grade(average))

name=input("Enter Student Name")
m1=int(input("Enter MArks of Subject 1:"))
m2=int(input("Enter Marks of Subject 2:"))
m3=int(input("Enter Marks of Subject 3:"))

Student_report("Taha",m1,m2,m3)

