
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
def calc (v1 = None, v2 = None, act = None):
    if act == "+":
        result = sum(a=v1, b=v2)
    elif act == "-":
        result = dif(a=v1, b=v2)
    elif act == "*":
        result = mult(a=v1, b=v2)
    elif act == "**":
        result = pow(a=v1, b=v2)
    elif act == "/":
        while v2 != 0:
            result = div(a=v1, b=v2)
            break
        else:
            print("division by 0 is impossible")
            v2 = float (input("type your value" "\n"))
    return result
while respond == "yes":
    v1 = float (input("type your value" "\n"))
    result = v1
    act1 = ""
    while act1 != "=":
        act1 = input ("Type operation" "\n")
        if act1 != "=":
            v2 = float (input("type your value" "\n"))
            result = calc (result, v2, act1)
        
    else:
        print("Your value is:", result)
        respond = input ("Do you want to continue counting?" "\n")
else:
    print ("See you later then")