#detect weather the input name contains less than 10 characters or not 

a=input("ENTER DESIRED NAME:")
if(len(a)<9):
    print("THE NAME HAS LESS THAN 10 CHARACTERS")
else:
    print("THE NAME HAS MORE THAN OR EQUAL TO 10 CHARACTERS")