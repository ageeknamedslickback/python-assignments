#Penelope Fernandez
#CMIS 102/6986
#7/22/2022
#Week 6 Discussion

#Simple program where you are asked to sign up for it.

def count_digits(word):
    """Count the number of digits in a word."""
    digit_count = 0
    for each in word:
        if each.isdigit() is True:
            digit_count += 1
    
    return digit_count

def main():

#welcome message    
    print('\nWelcome, this is your first time using this program.\nPlease, follow the next steps to create an account:')

#setting up the variables the user will prompt
    name = ''
    lastname = ''
    pin = ''
    secret = ''

    name = str(input('\nEnter your first name: '))
    print('Great, you will be signed up with the username of ',name.capitalize() ,)

    lastname = str(input('\nEnter your lastname: '))

    # Altered program to count the number of digits in the user input
    print(f"Your first name has {count_digits(name)} digit(s)")
    print(f"Your last name has {count_digits(lastname)} digit(s)")

#string condition 'in' to find matching initials with mines    
    if ('p' or 'f' or 'v') in name[0]:
        print('\n.....By the way, we have initials in common!, mines are PFV ' )
    else:
            None 
    if ('p' or 'f' or 'v') in lastname[0]:
        print('\n.....By the way, we have initials in common!, mines are PFV ' )
    else:
            None 
        
    pin = str(input('\nPlease, create a 4-digit PIN for your account: '))
    lenght = len(pin)   #the PIN will be strictly composed by 4 numbers, otherwise 'invalid PIN' will display
    if lenght == 4:
        print('\nYour PIN is successfully set, do not forget, it stars with the number', pin[0])
    else:
        print('\nInvalid PIN')

    print(f"Your pin has {count_digits(pin)} digit(s)")

    secret = str(input('\nExtra security question:\nIn which city you were born? ' ))
    slen = len(secret)
    print('\nIf you are ever asked the security question, the',len(secret),'characters will have to match') 

    print('\nOk, you are all set ', name.capitalize(),'',lastname.capitalize(), '!')

    print(f"Your secret has {count_digits(secret)} digit(s)")

#Initials from the user
    iname = name[0]
    ilastname = lastname[0]

    print('\n\n *accept all the terms and conditions you will never read...: ',iname.capitalize()+ilastname.capitalize())



main() 
