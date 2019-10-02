def login():
    username = input("Enter Username")
    password = input("Enter Password")
    if username == "admin" and password == "1234":
        return showMenu()
    else:
        print("Login Fale")

def showMenu():
    print("---Hello----")
    print("Choose 1=Calculate Vat:")
    print("Choose 2=Calculate Price")
    return menuSelect()

def menuSelect():
    choose = int(input(">>"))
    if choose == 1:
        print("Vat is" , vatCalculate(float(input("Price: "))))
    elif choose == 2:
        print("Total Prise is " , priceCalculate())

def vatCalculate(totalPrice):
    vat = 7
    result = (totalPrice * vat) / 100
    return result

def priceCalculate():
    price1 = float(input("First Product"))
    price2 = float(input("Second Product"))
    return vatCalculate(price1+price2)

login()