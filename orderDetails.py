class OrderDetails:
    
    def __init__(customer,order):
        self.customer = customer
        self.order = order
        self.orderPrice = 0

    def calculateOrderPrice():
        for item in self.order.items:
            self.orderPrice += int(item.split(sep=':')[1])
        