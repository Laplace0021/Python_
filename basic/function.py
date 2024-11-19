y = "esaer"
x = 5
def variable():
    global y,x 
    x = 1
    y = "asr"
    print(y,x)
variable()
print(y,x)