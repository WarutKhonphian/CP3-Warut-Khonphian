listMenu = []
listPrice = []

def showBill():
    print("-------My Food-------")
    totaPrice = 0
    for i in range(len(listMenu)):
        print(listMenu[i],listPrice[i])
        totaPrice = totaPrice + int(listPrice[i])
    print("ราคารวมสินค้า",totaPrice)

while True:
    menuName = input("please Enter your menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        listMenu.append(menuName)
        listPrice.append(menuPrice)
showBill()