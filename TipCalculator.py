################ Tip Calculator ######################

# Printing a welcome message
print("Welcome to Bhim's tip calculator!\n")

# Getting user input for the total bill, tip percentage, and number of people
Bill = float(input("What was the total bill? : $"))
Tip = int(input("How much tip would you like to give? : %"))
People = int(input("How many people to split the bill? :"))

# Calculating the tip amount as a percentage of the total bill
Tip_as_Percent = Tip / 100
Total_bill_Amount = Bill * Tip_as_Percent

# Calculating the total bill including the tip
Total_Bill = Bill + Total_bill_Amount

# Calculating the amount each person should pay
Bill_per_Person = Total_Bill / People

# Using Rounding function for the final amount to two decimal places
#Final_Amount = round(Bill_per_Person, 2) #it's not working for final amount as a string with two decimal places.

# That's why using Formatting function the final amount as a string with two decimal places
Final_Amount = "{:.2f}".format(Bill_per_Person)

# Displaying the result
print(f"Each person should pay : ${Final_Amount} ")
