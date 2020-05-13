# This component will calculate the total sales required and the price per product needed to reach the desired
# amount of profit


product_number = int(input("Number of product: "))
total_cost = int(input("Total cost: $"))
profit = int(input("Desired profit: $"))
total = total_cost+profit
print("required sales: ${}".format(total))
print("Price per product: ${}".format(total/product_number))