systemMenu = {"ไก่ทอด": 35, "เป็ดทอด": 45, "ปลาทอด": 55, "ผักทอด": 20}

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
        listMenu.append([menuName,systemMenu[menuName]])
showBill()