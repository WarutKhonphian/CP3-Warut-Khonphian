def login():
    user = input("Username : ")
    password = input("password : ")
    if user == "warut" and password == "1234":
        return True
    else:
        return False
def showMemu():
    print("-----iShop-----")
    print("1. Vat. Calculator")
    print("2. Price Calculator")
def menuSelect():
    userSelected = int(input(">>"))
    return userSelected

def vatCalculate(totalPrice):
    vat = 7
    result = int(totalPrice) + ((int(totalPrice) * vat) / 100)
    return result
def priceCalculate():
    price1 = int(input("1st Product price = "))
    price2 = int(input("2nd Product price = "))
    return  vatCalculate(price1 + price2)

def iShopProgram():
    if login():
        showMemu()
        select = menuSelect()
        if select == 1:
            print(vatCalculate(input("Price : ")))
        elif select == 2:
            print("Total Price :",priceCalculate())
    else:
        print("Log in Failue")
        print("----------------------------------")
        iShopProgram()

iShopProgram()
    