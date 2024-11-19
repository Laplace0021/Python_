x=int(input("enter first num: "))
operation=input("enter opertation + or -: ")
y=int(input("enter sec num: "))
if operation == "+" :
   global c 
   c=x+y
if operation == "-" :
    c=x-y
print(c)