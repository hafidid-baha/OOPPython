from customer import Customer
from order import Order
from orderDetails import OrderDetails

c = Customer('hafid','id-baha',2000)
o = Order('OR546546556')

# add items to the order
o.addItem('item1','200')
o.addItem('item2','50')
o.addItem('item3','220')
o.addItem('item4','100')

# creating the order details
od = OrderDetails(c,o)
print(od)

# apply the order
od.applyOrder()

# print the customer credit after applying the order
print(str(c.credit))
