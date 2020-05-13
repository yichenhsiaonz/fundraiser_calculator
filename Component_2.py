# This component loops taking in the names and prices of components and multiplies the prices by the number
# of product made
# This will be tweaked slightly to accommodate the fixed prices in the final program.


def double_input(question_1, question_2, iscomponent):
    input_1 = input(question_1).lower()
    if input_1 == "end" and iscomponent == 1:
        return "END"
    input_2 = 0
    while input_2 == 0:
        try:
            input_2 = int(input(question_2))
        except ValueError:
            print("Please enter an integer greater than 0!!!")
    return [input_1, input_2]


product_name_number = double_input("Enter the product name: ", "How much of the product will be produced?: ", 0)
print()
variable_cost_loop = 0
variable_cost_list = []
print("Type \"end\" to end the loop")
while variable_cost_loop == 0:
    variable_name_price = double_input("Enter the name of a component of the product: ",
                                       "How much will each of this component cost?: ", 1)
    if variable_name_price == "END":
        variable_cost_loop = 1
    else: variable_cost_list.append(variable_name_price)
print()
print("{} of {} will be produced.".format(product_name_number[1], product_name_number[0]))
total_variable_price = 0
for x in variable_cost_list:
    print("{}: ${}".format(x[0], x[1]*product_name_number[1]))
    total_variable_price += x[1]*product_name_number[1]
print("Total variable costs: ${}".format(total_variable_price))