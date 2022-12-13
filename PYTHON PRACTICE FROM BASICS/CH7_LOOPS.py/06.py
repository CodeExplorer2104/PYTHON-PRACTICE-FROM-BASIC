#factorial of the given number

num=int(input("ENTER DESIRED NO."))

fact=1

 
for i in range (1,num+1):

    fact=fact*i

print(f"FACTORIAL OF {num} IS {fact}")

