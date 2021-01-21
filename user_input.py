def user_input_numlist():
    numList = []
    result = 0
    for i in range(10):
        user_input = int(input("Enter any numbers: "))
        try:
            numList.append(user_input)
            if user_input % 2 == 0:
                result += user_input
        except ValueError:
            print("Incorrect value. That's not an int!")
        
    return result


sum_of_even_num  = user_input_numlist()
print("The sum of the even numbers in user_list is: ", sum_of_even_num)
