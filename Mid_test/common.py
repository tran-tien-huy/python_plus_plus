# Function to check whether the input is a string, a charater, a special character, or a number.
def char_check(input=""):
    if(len(input) == 1):
        if ((int(ord(input)) >= 65 and
            int(ord(input)) <= 90) or
            (int(ord(input)) >= 97 and
            int(ord(input)) <= 122)):
            return 0
        elif (int(ord(input)) >= 48 and
                int(ord(input)) <= 57):
            return 1
        else:
            return -1
    elif(len(input)>1):
        for i in input:
            flag = char_check(i)
            if(flag <=0):
                break
        return flag
    else:
        return -2

def user_input(message="", format=">0"):
    n = input(message)
    if format == ">0":
        while True:
            if(char_check(n) == 1):
                n = int(n)
                if n >= 0:
                    break
            n = input(message)

    return n
