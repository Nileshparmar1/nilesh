'''
Create class in new file for sale  in that there is one variable which keeps 
    track of Product Selling Date,  Quantity, Customer Name, Basic Price, Total Tax & Total Price,
    sale order number (Auto incremented number ie. SO/00001, SO/00002)

1)Sale :- At the time of Sale there should be set Selling date, quantity,
    Auto Generate Sale Number customer name, basic price , 
    total tax (will be calculated from get_tax method) in sale class attribute.
    (Which is Sale Class Method Sale()) & update in Product class Attribute Available Quantity,
    Sale Order number and profit or Loss(Which is Product Class method Sale inherits from sale class).
'''
from tax import tax_calculate
class Sales_product:
    
    def sale(self):
        product_name=dict()
        product_name=input("Enter Product Name: ")
        product_name['quantity']=quantity
        
        
        
        return    
Sales_obj=Sales_product()
