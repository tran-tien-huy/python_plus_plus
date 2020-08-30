def count_character_in_str_using_dict(input_str):
    count_dict = {}

    for i in input_str:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict
def count_character_in_str_using_set(input_str):
    temp_set = set(input_str)
    return {i : input_str.count(i) for i in temp_set}

if __name__ == "__main__":
    input_str = input("Please enter your string input: ")
    print(count_character_in_str_using_dict(input_str))
    print(count_character_in_str_using_set(input_str))