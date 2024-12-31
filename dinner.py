# Developed by: Ariana F
# Date: Feb 4, 2022
# Desc: A program to inquire invitees about their dietary preferences.
#       The program also inquires the tip amount, shows number of invitees who ordered each meal
#       in accordance to their preference, total cost before & after tax, and final cost with tip.
# Inputs: Number of invitees, order details for each invitee, tip percent
# Outputs: order questions and information for each invitee and cost details.

# Declare and initialize variables: numInvitees, Y, counters
numInvitees= int(input("Please enter the number of invitees:"))
print(" "*20)
Y= range(numInvitees)
inviteesCount=0
pizza=0
pasta=0
falafel=0
steak=0
beverage=0
#Loop to gather order details for each invitee
for i in(Y):
    inviteesCount+=1
    print("Please enter the order details for invitee Number",inviteesCount,'/',numInvitees)
    ansKeto= str(input("Do you want a keto friendly meal?"))
#Boolean variables to store response. y in lowercase means yes, anything else means no.
    if ansKeto=="y":
        ansKeto = True
    else:
        ansKeto = False
    ansVegan= str(input("Do you want a vegan meal?"))
    if ansVegan=="y":
        ansVegan = True
    else:
        ansVegan = False
    ansGlutenfree= str(input("Do you want a Gluten-free meal?"))
    if ansGlutenfree == "y":
        ansGlutenfree = True
    else:
        ansGlutenfree = False
# the print statement prints "-" for organization and aesthetics
    print("-"*20)
# Boolean variables to match the dietary preference with the meal, and counts the
# number of invitees who ordered that meal.
    if ansKeto == True and ansVegan == True and ansGlutenfree == False:
        pizza += 1
    elif ansKeto == False and ansVegan == True and ansGlutenfree == False:
        pasta += 1
    elif ansKeto == True and ansVegan == True and ansGlutenfree == True:
        falafel += 1
    elif ansKeto == True and ansVegan == False and ansGlutenfree == True:
        steak += 1
    else:
        beverage += 1
# Variable that lets user input amount of tip
tipAmount = int(input("How much do you want to tip your server (% percent)?"))
print(" "*20)
#prints how many people ordered each meal, and the cost is found by multiplying number of orders by price.
print("You have", numInvitees, "invitees with the following orders:")
print(pizza,"invitees ordered Pizza. The cost is:", "$%.2f"%(pizza*44.50))
print(pasta,"invitees ordered Pasta. The cost is:", "$%.2f"%(pasta*48.99))
print(falafel,"invitees ordered Falafel. The cost is:", "$%.2f"%(falafel*52.99))
print(steak,"invitees ordered Steak. The cost is:", "$%.2f"%(steak*49.60))
print(beverage,"invitees ordered only beverage. The cost is:", "$%.2f"%(beverage*5.99))
print(" "*20)
# variables that shows total cost excluding the tip and tax, cost after tax,
# total cost w/ tip and tax is imbedded in last print statement to ensure
# code is shorter. Variable with a constant tax of 13%.
totalAmount = (pizza*44.50 + pasta*48.99 + falafel*52.99 + steak*49.60 + beverage*5.99)
TAX = 0.13
totalCostAfterTax = totalAmount+(totalAmount*TAX)

print("The total cost before tax is","$%.2f"%(totalAmount))
print("The total cost after tax is","$%.2f"%(totalCostAfterTax))
print("The total cost after %d%% tip is $%.0f"%(tipAmount,totalCostAfterTax+(totalCostAfterTax*tipAmount/100)))
