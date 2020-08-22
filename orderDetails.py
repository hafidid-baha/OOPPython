class OrderDetails:
    
    def __init__(customer,order):
        self.customer = customer
        self.order = order
        self.orderPrice = 0
        calculateOrderPrice()

    def calculateOrderPrice(self):
        for item in self.order.items:
            self.orderPrice += int(item.split(sep=':')[1])

    def applyOrder(self):
        self.customer.checkout(self.orderPrice)

    def __str__(self):
        print(self.customer.fname+" "+self.customer.lname)     
        print(len(self.customer.items)+" items ,price = "+self.orderPrice)   