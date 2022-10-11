

#Hubbard, CMIS 102

#Discussion Week 2



def main():

    # simple program to determine the price for axe throwing. rate is $35 per guest per hour. 17% charge for insurance

    print("Welcome to the Detroit Axe Club. \n ***Guaranteed an unforgettable experience of drinking and axe throwing.***")



    #variables

    thrower = eval(input("How many people are in your party?\n"))

    hours = eval (input("How long is your stay (hours)?\n"))

    discount = eval(input("Do you have any discount amount?\n"))



    #total calculation



    rate= 35*thrower

    total= rate*hours



    #off set wildly high insurance cost by including into guest total as a "misc" fee

    actualTotal = total+(total*.17)

    dicounted_total = actualTotal - discount

    print("Inlucing service fee, Your total will be" , actualTotal, "\nYour discounted total will be", dicounted_total, "\nWear closed-toe shoes and have a great time! \n*Detroit Axe Club is not responsible for any alcohol nor Axe related injuries during your time here.*")

main()

