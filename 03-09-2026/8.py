# write a python program to calculate the final bill amount after applying a discount.
#The program should take the total bill ammount aas input from the user abd apply the discount according to the following rules.
#After calculating the discount, the program should display the discount amount and the final bill amount payable by the customer.

# Bill Amount                       # discount
# above 5000                        # 20 %
# 3000 to 5000                      # 10 %
# Below 3000                        # No Discount


bill = int(input("Enter bill: "))

if bill > 5000:
    d = bill * 20 / 100
elif bill >= 3000 and bill <= 5000:
    d = bill * 10 / 100
else:
    d = 0

print("Discount : ", d)
print("Final Bill : ", bill - d)