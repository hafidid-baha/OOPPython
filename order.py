class Order:

    def __init__(self,order_id):
        self.order_id = order_id
        self.items = []

    def __str__(self):
        return "order id id : "+str(self.order_id)

    def addItem(self,item,price):
        self.items.append(item+':'+price)
        return self.items

    def showItems(self):
        print(*self.items)