def user_input_numlist(numList):
    sum_list = 0
    numList = []
    for i in range(10):
        number = int(input("Enter numbers: "))
        try:
            numList.append(number)
            if number % 2 == 0:
            sum_list += number
        except ValueError:
            print("Incorrect value. That's not an int!")

    return result

print("The sum of the even numbers in user_list is: ", user_input_numlist(numList))
