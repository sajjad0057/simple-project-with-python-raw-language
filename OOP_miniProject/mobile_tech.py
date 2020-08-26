from product import Tech

class Mobile(Tech):
    def __init__(self,name,price,weight,color,screen,camera):
        Tech.__init__(self,name,price,weight,color) # if we want to use super() method instead of class name <Tech> we don't pass 'self' argument with constructor,,
        self.screen = screen                        # otherwise throw error,
        self.camera = camera

    def apply_discount(self):
        self.price = int(self.price - self.price * (Tech.discount/2)) # we can use class variable using <class_name.variable_name> or <super().class_variable_name>

    def __str__(self):
        return f'Name : {self.name} \n Price : {self.price}\n Weight : {self.weight} gm\n'\
               f' Color : {self.color} \n Screen : {self.screen}\n Camera: {self.camera} Mega.Pixel\n'


