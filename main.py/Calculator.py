
user_name = input("Hey, type your name:" "\n")
print ("Nice to meet you,", user_name )
print ("You are on the first python calculator")

print("would you like to count?")
respond = input()
result = None

while respond == "yes":
    
    first_value = input ("Type your first value" "\n")
    fv = int(first_value)
    operation = input ("what kind of operation you want to do" "\n")
    second_value = input ("Type your second value" "\n")
    sv = int(second_value)
    if operation == "+":
        result = fv + sv
    elif operation =='-':
        result =fv - sv
    elif operation == "*":
        result = fv * sv
    elif operation == "/":
        while sv!=0:
            result = fv / sv
        else:
            print (" devision by 0 is impossible, try something different")
            
    if result != None :
        given_result = float (result)
        print (given_result)
    respond = input("Continue counting?")
else:
    print ("See you soon then")

