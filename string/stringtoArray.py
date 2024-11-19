a = "hello world"

for x in a: #loop through var a
    print(x)
print("")
print(len(x)) #length of var a
print(len(a))
print(a[6]) #print var a index 6
print(a[3:5])
print("world" in a)
if "hello" not in a:
    print("yes, hello is not in a")
else :
    print("no, hello is in a")