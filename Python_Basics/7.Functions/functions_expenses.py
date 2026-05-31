
def find_total(expenses):
    '''
    This function takes expenses list as an input
    and return a total sum of that list
    :param expenses: list of input expenses
    :return: total expense
    '''
    total = 0
    for expense in expenses:
        total += expense
    return total

expenses_sergey = [30, 45, 70, 90]
expenses_sundar = [40, 23, 10, 85]

total = find_total(expenses_sergey)

print("Sergey's total expense: ", total)

total = find_total(expenses_sundar)

print("Sundar's total expense: ", total)


# Example for Function Arguments

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

total = sum_all(1,2,3,4,5)

print(f"\nSum of all numbers: {total}")

def company_info(**kwargs):
    if 'ticker' in kwargs:
        print("Ticker: ", kwargs['ticker'])
    if 'ceo' in kwargs:
        print("CEO: ", kwargs['ceo'])
    if 'revenue' in kwargs:
        print("Revenue:", kwargs['revenue'])


company_info(ticker='AAPL', ceo="Tim Cook", revenue="200 billion")



# Example for Calculating Volume of Cylinder

def find_cylinder_volume(radius, height=7):
    print("\nradius:", radius)
    print("height:", height)
    volume = 3.14*(radius**2)*height
    print(volume)
    return volume

r = 5
h = 10

print(find_cylinder_volume(r, h))





