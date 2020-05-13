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


product_name_number = double_input("Enter the product name: ",
                                   "How much of the product will be produced?: ", 0)
print()

variable_cost_loop = 0
variable_cost_list = []
print("Enter variable costs (costs that will change based on the number of product made)")
print("Type \"end\" to end the loop")
while variable_cost_loop == 0:
    variable_name_price = double_input("Enter the name of a variable cost of the product: ",
                                       "How much will this cost per product?: $", 1)
    if variable_name_price == "END":
        variable_cost_loop = 1
    else: variable_cost_list.append(variable_name_price)
print()

fixed_cost_loop = 0
fixed_cost_list = []
print("Enter fixed costs (costs that will not change based on the number of product made)")
print("Type \"end\" to end the loop")
while fixed_cost_loop == 0:
    fixed_name_price = double_input("Enter the name of the fixed cost: ",
                                    "How much will this cost?: $", 1)
    if fixed_name_price == "END":
        fixed_cost_loop = 1
    else: fixed_cost_list.append(fixed_name_price)
print()

profit = 0
while profit == 0:
    try:
        profit = int(input("How much profit would you like to make?: $"))
    except ValueError:
        print("Please enter a number above 0!!!")
print()

print("Number of {} produced: {}".format(product_name_number[0], product_name_number[1]))
print()

print("Variable costs:")
total_variable_price = 0
for x in variable_cost_list:
    print("{}: ${}".format(x[0], x[1]*product_name_number[1]))
    total_variable_price += x[1]*product_name_number[1]
print("Total variable costs: ${}".format(total_variable_price))
print()

print("Fixed costs:")
total_fixed_price = 0
for x in fixed_cost_list:
    print("{}: ${}".format(x[0], x[1]))
    total_fixed_price += x[1]
print("Total fixed costs: ${}".format(total_fixed_price))
print()

total_cost = total_variable_price + total_fixed_price
total = total_cost+profit
print("Required sales: ${}".format(total))
print("Price per product: ${}".format(total/product_name_number[1]))