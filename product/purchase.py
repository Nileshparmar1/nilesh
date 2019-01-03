'''
Create class for Purchase in that there is one variable which keeps track of 
Product Purchasing Date,  Quantity, Vendor Name(Seller Name), Basic Price, Total Tax & Total Price.
Purchase Order number (Auto incremented number ie. PO/00001, PO/00002)
'''
import datetime
from tax import tax_calculate
class Purchase_product(tax_calculate):
   
    def Purchase(self):
        print("\n============================")
        print("\n        Purchase            ")
        print("\n============================")
       
        product_name=input("Enter Product Name: ")
        product_type=input("Enter Type of Product: ")
        purchase_quantity=int(input("Enter Quantity: "))
        price=int(input("Enter price: "))
        Purchase_Date=datetime.date.today()
        #total_tax=tax_calculate.get_text(self,price,product_type)
        total_tax=Purchase_product_obj.get_tax(price,product_type)
        
        return Purchase_Date,product_name,purchase_quantity,price,product_type,total_tax

Purchase_product_obj=Purchase_product()
