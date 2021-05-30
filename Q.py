print("\U0001F929","*********************************welcome to my atm***************************","\U0001F197")
def language():
    if num==1:
        return "you choice english language"
    else:
        return "you choice marathi language" 
num=int(input("choose your language,1.english,2.marathi...."))
A=language()
print(A)

def pin_code():
    if A==1:
        i=0
        while i<3:
            pin=int(input("enter the pin number."))
            if pin==2050:
                print("your pin is correct")
                break
            else:
                print("your pin is incorrect")
            i=i+1
        else:
            print("card will block")
    else:
        i=0
        while i<3:
            pin=int(input("Thumcha pin no taka"))
            if pin==2050:
                print("Thumcha pin brobr aahe.")
                break
            else:
                print("Thumcha pin chukicha aahe.")
            i=i+1
        else:
            print("card band jala")
    return pin
Code=pin_code()

def options():
    if A==1:
        if Code==2050:
            amount=5000
            print("press 1 for balance enquiry")
            print("press 2 for withdraw")
            print("press 3 for deposite")
            print("press 4 for exit")
            option=int(input("choose any option"))
            if option==1:
                c=amount,"your total amount"
            elif option==2:
                withdraw=int(input("enter your withdraw money"))
                c=amount-withdraw,"your total amount"
            elif option==3:
                deposite=int(input("enter your desposite money"))
                c=amount+deposite,"your total amount"
            else:
                c="please collect your card"
                print("thanks  for visiting sir \madam")
            return c
    else:
        if Code==2050:
            amount=5000
            print("Thumche sgle paise1 dhaba")
            print("Paise baher kada 2 dhaba")
            print("Paise bhra 3 dhaba")
            print("Baher kada card 4 dhaba")
            option=int(input("option enter kra"))
            if option==1:
                c=amount,"mee total amount"
            elif option==2:
                withdraw=int(input("Thumala kiti paise kadayche aahe."))
                c=amount-withdraw,"total amount"
            elif option==3:
                deposite=int(input("Thumala kiti paise bhrayche aahe."))
                c=amount+deposite,"total amount"
            else:
                c="Card baher kada"
                print("Dhanyavad")
            return c

def main():
    print(Code)
    print(options())
main()
