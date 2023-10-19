
user_name = input("Hey, type your name:" "\n")
print ("Nice to meet you,", user_name )
print ("You are on the first python calculator")

print("would you like to count?")
respond = input()
result = None

while respond == "yes":
    value1 = int(input ("Type the value" "\n"))
    operation1 = input ("choose your operation: " "\n" "+" "\n" "-" "\n" "*" "\n" "/" "\n" "**")
    value2 = int(input ("Type the value" "\n"))
    operation2 = input ("choose your operation: " "\n" "+" "\n" "-" "\n" "*" "\n" "/" "\n" "**" "\n" "=" )
    if operation1 == "+":
            result = value1 + value2
    elif operation1 == "-":
        result = value1 - value2
    elif operation1 == "*":
        result = value1 * value2
    elif operation1 == "**":
        result = value1 ** value2
    elif operation1 == "/":
        while value2!=0:
            result = value1 / value2
        else:
            print (" devision by 0 is impossible, try something different")
            
    value3 = int(input ("Type the value" "\n"))
    operation3 = input ("choose your operation: " "\n" "+" "\n" "-" "\n" "*" "\n" "/" "\n" "**" "\n" "=" )
    if operation3 == "=":
        if operation1 == "+":
            result = value1 + value2
        elif operation1 == "-":
            result = value1 - value2
        elif operation1 == "*":
            result = value1 * value2
        elif operation1 == "**":
            result = value1 ** value2
        elif operation1 == "/":
            while value2!=0:
                result = value1 / value2
            else:
                print (" devision by 0 is impossible, try something different")
