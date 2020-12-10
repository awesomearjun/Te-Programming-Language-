var = ""
inp = input("te >> ")       

def prtText():
    global inp
    global var
    if inp == "print >> {print}":
        inp = input("Print Function >> ")
        print(inp)
        inp = input("te >> ")

def v():
    global inp
    global var
    if inp == "var >> {var}":
        inp = input("Variable >> ")
        var = inp
        inp = input("te >> ")
    if inp ==  "print >> {" + var + "}":
        print(var)
        inp = input("te >> ")

v()
prtText()