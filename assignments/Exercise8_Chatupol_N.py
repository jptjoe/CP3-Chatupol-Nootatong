UserName = input("Please enter UserName:")
Password = input("Please enter Password:")
price = 0
if (UserName == "customer" and Password == "password"):
    print("---------- ร้าน JPT Shop ยินดีต้อนรับ ----------")
    print("---------------------------------------")
    print("------------- กรุณาเลือกสินค้าที่ต้องการ -------------")
    print("1  มะม่วง ผลละ 10 THB")
    print("2  กล้วย หวีละ  30 THB")
    print("3  แอปเปิ้ล ผลละ 15 THB")
    MenuSelection = int(input(">>>"))
    if (MenuSelection == 1):
        product = "มะม่วง"
        price = 10
    if (MenuSelection == 2):
        product = "กล้วย"
        price = 30
    if (MenuSelection == 3):
        product = "แอปเปิ้ล"
        price = 15
    Quantity = int(input("จำนวน : "))
    print("ท่านซื้อ ", product, "ราคาทั้งหมด", price * Quantity , " THB" )
    print("--------- ขอบคุณสำหรับการซื้อสินค้าร้านเรา ----------")
else:
    print("incorrect UserName or Password")