#Author: Marcus Crowe
#Creation Date: 2/4/25

#Error Handling Function
def multTest():
    try:
        int_choice = int(input("Enter a number between 1 and 10: "))
    except ValueError:
        print('That is not a valid number!, Please enter a valid number between 1 and 10.')
    else:
        print(int_choice * 3.14)

multTest()

