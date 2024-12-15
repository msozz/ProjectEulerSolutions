
THE_STRING = "..." #snipping out the 1000 digit number

products = []

for index in range(988):
    substring = THE_STRING[index:index+13]
    product = 1
    for digit in substring:
        product *= int(digit)
    products.append(product)

print(max(products))