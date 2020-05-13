# This component takes text and prints it back to the user


def user_input():
    input_loop = 0
    while input_loop == 0:
        try:
            item = input("What are you selling?")
            amount = int(input("How many will be made?"))
            return [item, amount]
        except ValueError:
            print("Please enter a number!!!")


text = user_input()
print("Number of {}: {}".format(text[0], text[1]))
