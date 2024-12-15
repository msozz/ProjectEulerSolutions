square = []
def counting(a, b):
    for number in range(a, b + 1):
        square.append(number**2)
    number_range = range(a, b + 1)
    number_range_square_root = sum(number_range)**2
    print(number_range_square_root - sum(square))
counting(1, 100)