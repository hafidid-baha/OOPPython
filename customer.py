class Customer:

    def __init__(self,fname,lname,credit):
        self.fname = fname
        self.lname = lname
        self.credit = credit

    def __str__(self):
        return self.fname+" "+self.lname

    def checkout(self,price):
        self.credit = self.credit - price