listMenu = []

def showBill():
    print("-------My Food-------")
    totaPrice = 0
    for i in range(len(listMenu)):
        print(listMenu[i][0],listMenu[i][1])
        totaPrice = totaPrice + int(listMenu[i][1])
    print("ราคารวมสินค้า",totaPrice)

while True:
    menuName = input("please Enter your menu : ")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price : ")
        listMenu.append([menuName,menuPrice])
showBill()
