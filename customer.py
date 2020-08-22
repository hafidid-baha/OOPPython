class Customer:

    __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

    __str__(self):
        return self.fname+" "+self.lname