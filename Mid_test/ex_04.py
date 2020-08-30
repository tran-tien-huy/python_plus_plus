import common
def calculate_price_by_kwh(input_kwh):
    price = 0
    if input_int <= 100:
        price = 1500
    elif input_int <= 300:
        price = 2000
    else:
        price = 3000
    return price


if __name__ == "__main__":
    while True:
        input_int = common.user_input("Please enter a positive kwh: ")
        if input_int > 0:
            break
    price = calculate_price_by_kwh(input_int)
    print(f"Electricity bill this month: {price} * {input_int} * 30 = {price * input_int *30}")