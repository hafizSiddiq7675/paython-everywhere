
# The CellPhone class holds data about a cell phone.
class CellPhone:
    def  __init__(self, manufact, model, price):
        self.__manufact = manufact
        self.__model = model
        self.__retail_price = price

# The set_manufact method accepts an argument for the phone's manufacturer.
    def set_manufact(self, manufact):
        self.__manufact = manufact

# The set_manufact method accepts an argument for the phone's model.
    def set_model(self, model):
        self.__model = model

# The set_manufact method accepts an argument for the phone's price.
    def set_retail_price(self, price):
        self.__retail_price = price

# The get_manufact method returns the phone's manufact number.
    def get_manufact(self):
        return self.__manufact

# The get_manufact method returns the phone's model.
    def get_model(self):
        return self.__model
        
# The get_manufact method returns the phone's price.
    def get_retail_price(self):
        return self.__retail_price
