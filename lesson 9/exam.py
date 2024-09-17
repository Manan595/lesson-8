medicalcause=input("do your have medical cause yes or no ")
attendence=int(input("enter the attendence of the student"))
if medicalcause=='yes':
    print('you are allowed ')
else:
    if attendence>=75:
     print('alowed')
    else:
       print('you are not allowed ')


