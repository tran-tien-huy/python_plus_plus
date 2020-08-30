import common
def check_prime_number(input):
    flag = 0
    j = 2
    while j <= input ** (1 / 2):
        if (i % j == 0):
            flag = 1
            break
        j += 1
    return flag == 0
if __name__ == "__main__":
    input_int = int(common.user_input("Please enter a number: "))
    result_set = set()

    for i in range(1, input_int):
        if (i == 2):
            result_set.add(i)
        elif (i > 2):
            if(check_prime_number(i)):
                result_set.add(i)
    print(result_set)