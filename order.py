class Order:
    
    items = []

    def __init__(self,order_id):
        self.order_id = order_id

    def __str__(self):
        return "order id id : "+str(self.order_id)