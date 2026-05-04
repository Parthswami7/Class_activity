class Computer:
    def __init__(self):
        self.__maxprice = 700
    def sell(self):
        print("Selling price : {}".format(self.__maxprice))
    def set_Maxprice(self, price):
        self.__maxprice = price 
c = Computer()
c.sell()
c.__maxprice = 800
c.sell()
c.set_Maxprice(100)
c.sell()
c.__maxprice