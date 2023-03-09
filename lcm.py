#defining a funtion to calculate lcm
def calculate_lcm(x,y):
    #selecting the greater number
    if x>y:
        greater=x
        else:
            greater=y
            while(True):
                if((greater%x==0)and(greater%Y==0)):
                    lcm=greater
                    break
                greater+=1
                return lcm
            #taking input from user
            num1=int(input("enter the number:"))
            num2=int(input("enter the number:"))
            #printing the result for the user
            print("the L.C.M. of",num1,"and",num2,"is",calculate_lcm(num1,num2))
