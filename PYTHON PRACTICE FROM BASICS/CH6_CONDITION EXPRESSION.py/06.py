#write a program to calculate the grade of a student from his marks from the following scheme:

a=int(input("ENTER YOUR MARKS"))

if(a>=90 and a<=100):
    print("YOUR GRADES ARE EXCELLENT")
elif(a>=80 and a<90):
    print("YOUR GRADES ARE A")
elif(a>=70 and a<80):
    print("YOUR GRADES ARE B")
elif(a>=60 and a<70):
    print("YOUR GRADES ARE C")
elif(a>=50 and a<60):
    print("YOUR GRADES ARE D")
else:
    print("YOU FAILED")