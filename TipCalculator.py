################ Tip Calculator ######################

print("Welcome To Bhim's Tip Calculator\n")

Total_Bill = float(input("What was the total Bill? : $"))

Tip_Percentage = int(input("What percentages tip would you like to give? : %"))

Total_People = int(input("How many people to split the Bill? : "))

''' 
############### This is the Multi-Line Comments ################

# Formula for percentage calculation :
# (Value / Total Value) * 100 %
# For Example :

Find 15% of 500

(15*100) / 500

'''

a = (Tip_Percentage * 100) / Total_Bill

Splited_Bill = a / Total_People

print("Each person should pay : $", Splited_Bill)