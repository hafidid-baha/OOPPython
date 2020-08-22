from customer import Customer
from order import Order

c = Customer("hafid","id-baha")
print(c)

o = Order(111)
o.addItem('tid')
o.addItem('javel')
o.showItems()