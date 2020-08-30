def find_index_max_character_in_string(input_str = ""):
    max_index = 0
    for i in range(len(input_str)):
        if (input_str[max_index] < input_str[i]):
            max_index = i
    return max_index

def find_index_min_character_in_string(input_str= ""):
    min_index = len(input_str) - 1
    for i in range(len(input_str)):
        if (input_str[min_index] > input_str[i]):
            min_index = i
    return min_index
if __name__ == "__main__":
    input_str = input("Please enter your string input: ")
    min_index = find_index_min_character_in_string(input_str)
    max_index = find_index_max_character_in_string(input_str)

    print(f"Max character of string {input_str} is {input_str[max_index]}")
    print(f"Max character of string {input_str} is {input_str[min_index]}")