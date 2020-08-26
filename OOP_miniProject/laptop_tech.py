from product import Tech

class Laptop(Tech):
    def __init__(self,name,price,weight,color,ram,cpu,storage):
        super().__init__(name,price,weight,color)  # if we want to use class name <Tech> instead of  super() method we must be pass 'self' argument with constructor,,
        self.ram=ram                               # otherwise throw error,
        self.cpu=cpu
        self.storage=storage

    def set_double_price(self):
        self.price = 2 * self.price

    def change_specs(self,ram,storage):
        if ram > self.ram or storage > self.storage:
            self.price =self.price + 10000
        elif ram < self.ram or storage < self.storage:
            self.price = self.price - 10000

        self.ram = ram
        self.storage = storage

    def __str__(self):
         return f'Name : {self.name} \n Price : {self.price}\n Weight : {self.weight} kg \n'\
                f' Color :  {self.color} \n RAM : {self.ram} GB \n CPU: {self.cpu}\n'\
                f' Storage: {self.storage} TB \n'
