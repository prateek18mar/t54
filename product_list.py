# Element of list should be replaced with the product of other element of the list

inputl = [1, 2, 3, 4]


# output = [24,12,8,6]

def product():
    # set a counter to 1
    prod = 1

    # Store the sum of all the element in the list
    for i in range(len(inputl)):
        prod *= inputl[i]

    # Divide the product by the number and store it in a list
    for i in range(len(inputl)):
        inputl[i] = prod // inputl[i]
    print(inputl)


product()
