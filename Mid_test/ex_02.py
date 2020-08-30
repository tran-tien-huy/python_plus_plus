import common
def sum_split_int(input_int):
    sum = 0
    for i in str(input_int):
        sum+=int(i)
    return sum
if __name__ == "__main__":
    while True:
        input_int = common.user_input("Please enter a positive integer: ")
        if input_int > 0:
            break
    print(sum_split_int(input_int))