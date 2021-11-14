def is_even(x):
    if x % 2 == 0:
        return 'it is even'
    elif x % 2 != 0:
        return 'it is odd'
    else:
        return 'Number is float'


def calculator(product_price):
    # product price increased with 10%
    increased_price = product_price + ((product_price / 100) * 10)
    # after one month product price decreased with 35%
    decreased_price = increased_price - ((increased_price / 100)*35)
    return decreased_price

