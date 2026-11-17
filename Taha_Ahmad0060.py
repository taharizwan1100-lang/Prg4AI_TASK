
customers = {
    "M101": {"Name":"Ali","Unit": 80},
    "M102": {"Name":"Sara","Unit": 150},
    "M103": {"Name":"Hamza","Unit": 320},
}
print("Total Customers : ",len(customers))
print(customers)
def Get_New_Customer():
    name=input("Enter Name Of Customer") 
    M_No=input("Enter Meter Number")
    try:
        unit=int(input("Enter Customer"))
        if(units<0):
            print("Enter Valid Unit")
    except:
        print("Enter Units Greater Than Zero")
        unit=int(input("Enter Customer"))
    return name,M_No,unit


def calculate(unit):
    if(unit<0):
        print("Wrong Input")
    elif(unit<100):
        bill=unit*10
        print("Bill is :",bill)
        print("Meter Charges = 100 ")
        bill=bill+100
        print("Total Bill is :",bill)
    elif(unit<300):
        bill=unit*15
        print("Bill is :",bill)
        print("Meter Charges = 100 ")
        bill=bill+100
        print("Total Bill is :",bill)
    elif(unit>300):
        bill=unit*20
        print("Bill is :",bill)
        print("Meter Charges = 100 ")
        bill=bill+100
        print("Total Bill is :",bill)
    A_Bill=bill

a=int(input("input Total Number of customers to check : "))
for i in range(a):
    try:
        unit=int(input("Enter Units Consumed"))
    except(ValueError):
        print("Ente Valid Number")
        unit=int(input("Enter Units Consumed"))
    print("for Customer : ",i+1)
    calculate(unit)
name,M_No,unit=Get_New_Customer()
dic["M102"]["unit"]=200
print("Dictionary Updated")
print(customers)
choice=int(input("Enter '1' to add new Customers Details in Dictionary"))
if(choice==1):
    Get_New_Customer()
else:
    print("Invalid Choice")



