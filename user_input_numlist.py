def user_input_numlist(numList):
    result = 0
    for num in numList:
        if num % 2 == 0:
            result += num

    return result

numList = []
numbers = (input("Enter numbers seperated by commas: ").split(','))

for num in numbers:
    numList.append(int(num))

sum_of_even_num  = user_input_numlist(numList)
print("The sum of the even numbers in user_list is: ", sum_of_even_num)
