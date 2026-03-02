n=int(input("ENTER A NUMBER : "))
fact = 1
if(n<0):
    print("ENTER ONLY POSITIVE NUMBERS : ")
elif(n==0):
    print("1 IS THE FACTORIAL")
else:
    for i in range(1,n+1):
        fact=fact*i
        print(fact)
