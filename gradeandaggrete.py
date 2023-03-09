N=int(input("enter the total number of subjects"))
M=float(input("enter mark in maths"))
P=float(input("enter the mark in physics"))
B=float(input("enter the mark in biology"))
C=float(input("enter the mark in cs"))
total=M+P+B+C
A=total/4
print("total marks",total)
print("aggrete marks",A)
if(A>=75):
    print("distinction with all pass")
elif(A>=60 and A<75):
    print("grade is first class")
elif(A>=50 and A<60):
    print("grade is second class")
elif(A>=40 and A<50):
    print("grade is third class")
else:
    print("reappear")
      

   
