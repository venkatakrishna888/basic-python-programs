num = int(input("ENTER A NUMBER :"))
if(num<=1):
    print("NOT  PRIME")
else:
    for i in range(2,num):
        if(num%i==0):
            print("NOT PRIME")
            break
        else:
            print("PRIME")
            break
