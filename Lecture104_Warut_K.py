class Customer:
    name = ""
    laseName = ""
    age = 0
    def addCart(self):
        print("Added to ",self.name,self.laseName,"'s cart")


customer1 = Customer()
customer1.name = "Warut"
customer1.laseName = "Khonphian"
customer1.age = 30
customer1.addCart()

customer2 = Customer()
customer2.name = "Winsmoke"
customer2.laseName = "Sunji"
customer2.age = 20
customer2.addCart()

customer3 = Customer()
customer3.name = "Mokey"
customer3.laseName = "luffy"
customer3.age = 10
customer3.addCart()