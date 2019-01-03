'''
Create One Class for Product and one variable which keeps track of Product name, 
Type, Available Quantity, Sale Order Number, Purchase Order Number, Total Profit or Loss etc. 
'''
from purchase import Purchase_product
class Product(Purchase_product):
    def __init__(self):
        self.available_quantity=0
        self.total_profit_loss=0
        
product_object=Product()
Purchase_Date,product_name,purchase_quantity,price,product_type,total_tax=product_object.Purchase()
print("Date: ",Purchase_Date)
print("Name: ",product_name)
print("type:",product_type)
print("Quantity: %d \n Price: %d"%(purchase_quantity,price))
print(total_tax)



    
    