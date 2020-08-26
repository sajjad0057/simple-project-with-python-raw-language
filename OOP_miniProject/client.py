from mobile_tech import Mobile
from laptop_tech import Laptop
from product import Tech
from sales_person import SalesPerson
from datetime import date

phone_1 = Mobile('iphone_11',60000,500,'Black','1920 x 1080', 10)
phone_2 = Mobile('iphone_12',70000,580,'silver','1920 x 1080',30)
phone_3 = Mobile('iphone_13',80000,680,'light white','1920 x 1080',37)


laptop_1 = Laptop('hp Probook 450 g4',67000,1.5,'silver',8,'core i7',1)
laptop_2 = Laptop('ASUS g14',130000,1.6,'moon-light silver',16,'core i7',1)
laptop_3 = Laptop('Macbook pro 13',167000,1.5,'white',16,'core i7',0.512)


sales_person_1= SalesPerson(
    'sajjad',
    'hossain',
    40000,
    date(2020,8,18)
)


# Test Method
print(laptop_1)
print(laptop_3)

print(phone_1)
print(phone_2)

# Check Total No. of product

print(Tech.get_total_product())

# Shipping Cost

print(laptop_3.calculate_shipping_cost(10))

# setting The Double price for the 1st laptop
print(laptop_1.price)
laptop_1.set_double_price()
print(laptop_1.price)

# changing specs for laptop 2
print(laptop_2)
laptop_2.change_specs(24,2)
print(laptop_2)


# selling product by sales_person

sales_person_1.sell_product(phone_2)
sales_person_1.sell_product(phone_1)
sales_person_1.sell_product(laptop_3)
sales_person_1.sell_product(laptop_2)


# product sold
sales_person_1.display_sales()

# total product sold:
print(sales_person_1.total_product_sold())

# Calculate Commission
print(sales_person_1.calculate_commission(0.2))

#Sort the sold products by price

sales_person_1.sort_by_price()
sales_person_1.display_sales()

print(f'Joining date of sales man  {sales_person_1.first_name}  is : {sales_person_1.date_joined}')












