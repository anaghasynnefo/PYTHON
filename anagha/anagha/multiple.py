subject1=float(input("enter the marks for subject1:"))
subject2=float(input("enter the marks for subject2:"))
subject3=float(input("enter the marks for subject3:"))
subject4=float(input("enter the marks for subject4:"))
subject5=float(input("enter the marks for subject5:"))

total_marks=subject1 + subject2 + subject3 + subject4 + subject5
percentage=(total_marks/500)*100

if 100<=percentage>85:
    print("excellent")

elif 85<=percentage>75:
    print("very good")

elif 75<=percentage>60:
    print("good")
    
elif 60<=percentage>45:
    print("pass")
    
elif percentage<=45:
    print("fail")
    
elif percentage>=100:
    print("error")
    
else:
    print("its an error")
    
print("total marks  :",total_marks)
print("percentage  :",percentage,"%")


