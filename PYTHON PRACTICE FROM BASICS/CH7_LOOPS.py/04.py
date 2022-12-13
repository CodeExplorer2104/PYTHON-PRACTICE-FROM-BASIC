#number is prime or not

num=int(input("ENTER THE DESIRED NO."))
prime = True
for i in range (2,num):
    if(num%i==0 and num!=2):
        prime = False
        break
if prime:
    print("THIS NO. IS PRIME")
else:
    print("THIS NO. IS COMPOSITE")