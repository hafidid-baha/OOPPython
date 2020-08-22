class OrderDetails:
    
    def __init__(self,customer,order):
        self.customer = customer
        self.order = order
        self.orderPrice = 0
        self.calculateOrderPrice()

    def calculateOrderPrice(self):
        for item in self.order.items:
            self.orderPrice += int(item.split(sep=':')[1])

    def applyOrder(self):
        self.customer.checkout(self.orderPrice)

    def __str__(self):
        print(self.customer.fname+" "+self.customer.lname)     
        print(str(len(self.order.items))+" items ,price = "+str(self.orderPrice))   
        return ""