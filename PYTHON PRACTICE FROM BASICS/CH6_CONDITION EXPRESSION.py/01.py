#finding the greatest number out of the four inputs



num1 = int(input("ENTER NUMBER 1:"))
num2 = int(input("ENTER NUMBER 2:"))
num3 = int(input("ENTER NUMBER 3:"))
num4 = int(input("ENTER NUMBER 4:"))

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2
else:
    f2=num3

if(f1>f2):
    print(f1,"IS THE GREATEST")
else:
    print(f2,"IS THE GREATEST")