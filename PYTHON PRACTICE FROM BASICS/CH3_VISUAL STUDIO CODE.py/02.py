letter=''' DEAR  <|NAME|> ,
YOU ARE SELECTED !
THANKYOU FOR JOINING US !
AND SUCCESFULLY COMPLETING THE COURSE!
DATE: <|DATE|>
'''
name=input("ENTER YOUR NAME \n")
date=input("ENTER DATE\n")
letter =letter.replace ("<|NAME|>",name)
letter =letter.replace("<|DATE|>",date)
print(letter)