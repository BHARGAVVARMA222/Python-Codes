from re import I
n=int(input("enter a number:"))
i=n
sum=0
while(i>0):
    r=i%10
    sum=sum+r*r*r
    i=int(i/10)
if(n==sum):
    print("amstrong number")
else:
    print("not an amstrong number")


 
    
    

