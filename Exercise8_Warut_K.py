userName = input("Username => ")
passWord  = input("Password => ")
if userName == "Customer" and passWord =="1234":
    print("!!!       Welcom to My Shop      !!!")
    print("--------------------------------")
    print("       กรุณาเลือกสินค้าที่ต้องการ       ")
    print("--------------------------------")
    print("กด 1 หนังสือการ์ตูน One Piece เล่มที่ 1 ")
    print("กด 2 หนังสือการ์ตูน One Piece เล่มที่ 2 ")
    print("กด 3 หนังสือการ์ตูน One Piece เล่มที่ 3 ")
    print("--------------------------------")
    selectItem = int(input( "ระบุรายการสินค้าที่ต้องการ =>"))
    print("--------------------------------")
    if selectItem == 1:
        print("สินค้าที่คุณเลือก คือ หนังสือการ์ตูน One Piece เล่มที่ 1 ")
        print("ราคาต่อเล่ม            35 บาท")
        print("--------------------------------")
        totalItem = int(input( "ระบุจำนวนสินค้าที่ต้องการ =>"))
        print("--------------------------------")
        print("สรุปลายละเอียด")
        print("หนังสือการ์ตูน One Piece เล่มที่ 1   จำนวน ",totalItem," ราคา",totalItem*35,"บาท")
        vat = ((totalItem * 35)*7)/100
        print("Vat 7%                                                                                      " ,vat,"บาท")
        print("ราคารวม                                                                                    ",(totalItem*35)+vat,"บาท")
    elif selectItem == 2:
        print("สินค้าที่คุณเลือก คือ หนังสือการ์ตูน One Piece เล่มที่ 2 ")
        print("ราคาต่อเล่ม            35 บาท")
        print("--------------------------------")
        totalItem = int(input( "ระบุจำนวนสินค้าที่ต้องการ =>"))
        print("--------------------------------")
        print("สรุปลายละเอียด")
        print("หนังสือการ์ตูน One Piece เล่มที่ 1           x"+totalItem,totalItem*35)
        vat = ((totalItem * 35)*7)/100
        print("Vat 7%                                " ,vat)
        print("ราคารวม                      ",(totalItem*35)+vat)
    elif selectItem == 2:
        print("สินค้าที่คุณเลือก คือ หนังสือการ์ตูน One Piece เล่มที่ 3 ")
        print("ราคาต่อเล่ม            35 บาท")
        print("--------------------------------")
        totalItem = int(input( "ระบุจำนวนสินค้าที่ต้องการ =>"))
        print("--------------------------------")
        print("สรุปลายละเอียด")
        print("หนังสือการ์ตูน One Piece เล่มที่ 1           x"+totalItem,totalItem*35)
        vat = ((totalItem * 35)*7)/100
        print("Vat 7%                                " ,vat)
        print("ราคารวม                      ",(totalItem*35)+vat)
    else:
         print("คุณทำรายการไม่ถูกต้อง กรุณาทำรายการใหม่")
         print("ขอบคุณครับ")
else:
    print("log in failed") 