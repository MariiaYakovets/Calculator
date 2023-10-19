
user_name = input("Hey, type your name:" "\n")
print ("Nice to meet you,", user_name )
print ("You are on the first python calculator")

print("would you like to count?")
respond = input()
result = None

def sum ( a = None, b = None):
    return a + b
def dif (a = None, b = None):
    return a - b
def mult (a = None, b = None):
    return a * b
def div (a = None, b = None):
    return a / b
def pow (a = None, b = None):
    return a ** b
def calc (v1 = None, v2 = None, act1 = None):
    if act1 == "+":
        var1 = sum(a=v1, b=v2)
    elif act1 == "-":
        var1 = dif(a=v1,b=v2)
    elif act1 == "*":
        var1 = mult(a=v1,b=v2)
    elif act1 == "**":
        var1 = pow(a=v1,b=v2)
    elif act1 == "/":
        while v2 != 0:
            var1 = div(a=v1,b=v2)
            break
        else:
            print("division by 0 is impossible")
            v2 = float (input("type your value" "\n"))
    return var1

while respond == "yes":
    v1 = float (input("type your value" "\n"))
    act1 = input ("Type operation" "\n")
    v2 = float (input("type your value" "\n"))
    var1 = calc (v1, v2, act1)

    act2 = input ("Type operation" "\n")
    if act2 != "=":
        v3 = float (input("type your value" "\n"))
    else:
        var1 = calc (var1, v3, act2)
    print("your value is", var1)
    respond = input ("Do you want to continue counting?" "\n")
else:
    print ("See you later then")