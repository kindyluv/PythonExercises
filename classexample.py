def get_digit(number, position):
    return number //(10**position)% 10

print(get_digit(527,2))