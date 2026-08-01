# TASK 3 : mini project : 
    
# KALYAN JWELLERS : 
# M 
# >  65
# purchase > 2lk - 3lk    20% 
# purchase > 3lk - 5lk 	30% 
# purchase > 5lk  	35% 
# <65
# purchase > 2lk - 3lk    10% 
# purchase > 3lk - 5lk 	20% 
# purchase > 5lk  	25% 
# F
# >  65
# purchase > 2lk - 3lk    25% 
# purchase > 3lk - 5lk 	35% 
# purchase > 5lk  	40% 
# <65
# purchase > 2lk - 3lk    15% 
# purchase > 3lk - 5lk 	25% 
# purchase > 5lk  	30% 
# ------------------------------------------------------------
# Enter your name : 
# Enter gender : 
# Enter age : 
# Enter product : Ring 
# Enter product gram : 20  
# current gold price (1 grm) : 5752
# -------------------------------------
# TOTAL GOLD RATE :  XXXXX 
# Making charges (1 gram)  : 845
# Total Making CHarges :    TOTAL GOLD  X  MAKING CHARGES 
# ---------------------------------------
# TOTAL AMOUNT : GOLD PRICE + TOTAL MAKING CHARG
# DISCOUNT :   25 (AUTOMATIC) 
# DIS- AMOUNT : except (making charges) 
# -----------------------------------------
# total net amount : 
# --------------------------------------------
# HINT : variables , input , conditional statements 

#Input Section
Name = input("Enter Your Name : ")
Gender = input("Enter Gender (M/F) :")
Age = int(input("Enter Your Age : "))
Product_Name = input("Enter The Product Name : ")
Product_Gram = float(input("Enter The Product Gram : "))
Gold_Price = float(input("Current Gold Price (1 Gram) : "))

#Calculations & Constants 
Total_Gold_Rate = Product_Gram  * Gold_Price
Making_Charges_Per_Gram = 845
Total_Making_Charges = Product_Gram * Making_Charges_Per_Gram

Discount_Purchase = 0
#Discount Percantage Depend On Gender, Age & Purchase
if Gender == 'M':
    if Age > 65:
        if Total_Gold_Rate > 200000 and Total_Gold_Rate < 300000:
           Discount_Purchase = 20
        elif Total_Gold_Rate > 300000 and Total_Gold_Rate < 500000:
           Discount_Purchase = 30
        elif Total_Gold_Rate > 500000: 
           Discount_Purchase = 35
    else:
        if Total_Gold_Rate > 200000 and Total_Gold_Rate < 300000:
           Discount_Purchase = 10
        elif Total_Gold_Rate > 300000 and Total_Gold_Rate < 500000:
           Discount_Purchase = 20
        elif Total_Gold_Rate > 500000: 
           Discount_Purchase = 25
else:
    if Gender == 'F':
        if Age > 65:
            if Total_Gold_Rate > 200000 and Total_Gold_Rate < 300000:
                Discount_Purchase = 25
            elif Total_Gold_Rate > 300000 and Total_Gold_Rate < 500000:
                Discount_Purchase = 35
            elif Total_Gold_Rate > 500000: 
                Discount_Purchase = 40
    else:
        if Total_Gold_Rate > 200000 and Total_Gold_Rate < 300000:
           Discount_Purchase = 15
        elif Total_Gold_Rate > 300000 and Total_Gold_Rate < 500000:
           Discount_Purchase = 25
        elif Total_Gold_Rate > 500000:
            Discount_Purchase = 30
#Final Calculation
Total_Amount = Total_Gold_Rate + Total_Making_Charges
Discount_Amount = (Total_Amount * Discount_Purchase) / 100

#Final Billing
Total_Net_Amount = Total_Gold_Rate - Discount_Amount

#Billing Output
print("\n----------------------------------------------------------------------")
print(f" Name : {Name}")
print(f" Gender : {Gender}")
print(f" Age : {Age}")
print(f" Product Name : {Product_Name}")
print(f" Product Gram : {Product_Gram}")
print(f" Current Gold Price : {Gold_Price}")
print("-----------------------------------------------------------------------")
print(f" Total Gold Rated : {Total_Gold_Rate}")
print(f" Making Chrges Per Gram : {Making_Charges_Per_Gram}")
print(f" Total Making Charges : {Total_Making_Charges}")
print("-----------------------------------------------------------------------")
print(f" Total Amount : {Total_Amount}")
print(f" Discount : {Discount_Amount}")
print("-----------------------------------------------------------------------")
print(f" Your Total Billing : {Total_Net_Amount}")
print("-----------------------------------------------------------------------")
# print("If You Want to Continue Excute This Code Enter 'Y' & Exit Code For Enter 'N'")
# if ch == 'Y' or 'y':
#    goto up
# else:
#    goto