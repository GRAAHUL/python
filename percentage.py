H=int(input("enter the total number of days"))
A=int(input("enter the number of days present"))
percentage=A/H*100
print("percentage of class attended",percentage)
if(percentage<75):
    print("student not allowed to sit in exam")
else:    
    print("student is allowed to sit in exam")
    
