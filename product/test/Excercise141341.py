import datetime
class purchase:
    
    purchase_data={}
    purchase_no=1
    
    def purchase_order(self,product_name):
        
        '''
            func   :-it is used to  purchase order
            param  :-
            return :-
        '''
        state='In Process'
        print(state)
        date=datetime.datetime.today().strftime('Date: %d/%m/%Y Time: %H:%M:%S')
        purchase.purchase_data[product_name]={'product_state':state}
        purchase.purchase_data[product_name]={'product_name':product_name}
        purchase.purchase_data[product_name]['purchase_date']=date
        purchase.purchase_data[product_name]['product_number']='PO/'+'0000'+str(purchase.purchase_no)
        
        purchase.purchase_no +=1
        
        purchase.confirm_purchase(self,product_name)
        
    def confirm_purchase(self,product_name):
        
        '''
            func   :- it is used to confirm the purchase order 
            param  :-product_name and its type is string
            return :-purchase_data and its type is dictionary.
        '''
        state='Done'
        purchase.purchase_data={'product_state':state}
        return purchase.purchase_data
    
#########################################################################################################    

class sales:
    
    sales_data={}
    sales_no=1
        
    def sales_order(self,product_name):
        
        '''
            func   :- it is used sales product
            param  :- product_name and it's type is string
            return :- it return sales details
        '''
        state='In Process'
        date=datetime.datetime.today().strftime('Date: %d/%m/%Y Time: %H:%M:%S')
        
        if not product_name in self.sales_data.keys():            
            sales.sales_data[product_name]={'product_state':state}
            sales.sales_data[product_name]={'product_selling_date':date}
            sales.sales_data[product_name]['sell_number']='SO/'+'0000'+str(sales.sales_no)
            
        else:
            #sales.sales_data[product_name]['sell_number']='SO/'+'0000'+str(sales.sales_no)
            for i in sales_data[product_name]:
                i['purchase_number']='SO/'+'0000'+str(sales.sales_no)
                i['']
                
            
        sales.sales_no += 1
        
        sales.confirm_sales(self,product_name)
    
    def confirm_sales(self,product_name):
        
        '''
            func   :- for sales product
            param  :- product_name and it's type is string
            return :- it return sales product detial's
        '''
        state='Done'
        sales.sales_data={'sales_state':state}
        
        return sales.sales_data
    
#########################################################################################################

class manufacture:
    
    manufacture_data={}
    manufacture_no=1
    
    def manufacture_order(self,product_name):
    
        '''
            func   :- it is used to manufacture new product
            param  :- product_name and it's type is string.

        '''
        date=datetime.datetime.today().strftime('Date: %d-%m-%Y Time: %H:%M:%S')
        state='In Process'
        manufacture.manufacture_data={'product_state':state}
        
        manufacture.manufacture_data[product_name]={'product_name':product_name}
        manufacture.manufacture_data[product_name]['product_name']=product_name
        manufacture.manufacture_data[product_name]['manufacture_date']=date
        manufacture.manufacture_data[product_name]['manufacture_number']=manufacture.manufacture_no
        
        manufacture.start_manufacture(self,product_name)
        
        
        
    
    def start_manufacture(self,product_name):
        
        '''
            func   :- for manufacture new product
            param  :- name define product_name and it's must be string
            return :- it return manufacture detial's
        '''
        state='Start'
        manufacture.manufacture_data={'product_state':state}
        
        manufacture.done_manufacture(self,product_name)
        
        
    def done_manufacture(self,product_name):
        
        '''
            func   :- for manufacture new product's
            param  :- name define product name and it's must string
            return :- it return manufacture detial's 
        '''
        state='Done'
        manufacture.manufacture_data={'Prodcut_state':state}
        
        return manufacture.manufacture_data
    
#################################################################################################################

class product:
    max_sale_purchase_price=0
    max_sale_discount=0.10
    purchase_tax=0.10
    sale_tax=0.15
    total_sales=0
    type={'stock','consumable','service'}

    
#################################################################################################################        

class my_company(purchase,sales,manufacture,product):
    purchase_data={}
    manufacture_data={}
    sales_data={}
    final_stock_data={}
    raw_matirial_data={}
    manufacture_no=1
    purchase_no=1
    sales_no=1
    min_stock_level=10
    
    
    def __init__(self):
        
        self.company_name="Amazon"
        self.city="Rajkot"
        self.state="Gujrat"
        self.country="India"
        
    def Company_info(self):
        print(self.company_name,self.city,self.state,self.country)
        
    ################################################################################################
       
    def create_purchase_order(self):
        
        '''
            func   :- it is used to purchase new product
            param  :- 
            return :- show purchase product
        '''       
        
        product_name=input("Enter Product Name : ")
        product_type=input("Enter Product Type (stock / consumable / service ) : ")
        product_quantity=int(input("Enter Product quantity : "))
        product_price=int(input("Enter Product Price : "))
        date=datetime.datetime.today().strftime('Date : %d-%m-%Y Time : %H:%M:%S')
        
        if product_type=='stock' and product_quantity < my_company_obj.min_stock_level:
            print("\nPurchase product More than minimum stock level",self.min_stock_level)
        
        if not product_name in my_company_obj.purchase_data.keys():
    
            my_company_obj.purchase_order(product_name)
        
            unit_price= product_price / product_quantity
        
            my_company_obj.purchase_data[product_name]={'product_name':product_name}
            my_company_obj.purchase_data[product_name]['product_quantity']=product_quantity
            my_company_obj.purchase_data[product_name]['product_price']=product_price
            my_company_obj.purchase_data[product_name]['unit_price']=unit_price
            my_company_obj.purchase_data[product_name]['purchase_date']=date
            my_company_obj.purchase_data[product_name]['product_type']=product_type
            
            my_company_obj.purchase_data[product_name]['purchase_number']='PO/'+'0000'+str(my_company_obj.purchase_no)
        else:
        
            my_company_obj.purchase_data[product_name]['product_quantity'] +=product_quantity
            my_company_obj.purchase_data[product_name]['product_price'] +=product_price
            unit_price= product_price / product_quantity
            
            
            my_company_obj.purchase_data[product_name]['purchase_date']=date
            my_company_obj.purchase_data[product_name]['purchase_number']='PO/'+'0000'+str(my_company_obj.purchase_no)
        
            my_company_obj.purchase_no +=1
            
    ################################################################################################
    
    def create_sales_order(self):
        
        '''
            func   :- for sales product
            param  :- none
            return :- show sales product details
        '''
        product_name=input("Enter Product Name : ")
        date=datetime.datetime.today().strftime('Date : %d-%m-%Y Time : %H:%M:%S')
        
        if not product_name in my_company_obj.purchase_data.keys():
            
            print("Entered Product is Not Available")    
        if not product_name in my_company_obj.sales_data.keys():
                product_quantity=int(input("Enter Product quantity : "))
                product_price=int(input("Enter Product Price : "))
                vendar_name=input("Enter Vendor Name : ")
            
                #my_company_obj.sales_order(product_name)
            
                my_company_obj.sales_data[product_name]={'product_name':product_name}
                my_company_obj.sales_data[product_name]['vendor_name']=vendar_name
                my_company_obj.sales_data[product_name]['product_quantity']=product_quantity
                my_company_obj.sales_data[product_name]['product_date']=date
                my_company_obj.sales_data[product_name]['product_price']=product_price
                my_company_obj.sales_data[product_name]['sales_number']='SO/'+'0000'+str(my_company_obj.sales_no)
                
                #my_company_obj.sales_no +=1
                
                my_company_obj.purchase_data[product_name]['product_quantity'] -=product_quantity
                unit_price=my_company_obj.purchase_data[product_name]['unit_price']
                
                my_company_obj.purchase_data[product_name]['product_price'] -=int(product_quantity*unit_price)
                
                print("\n Product sales Successfully...")
                print(my_company_obj.confirm_sales(product_name))
        else:
            product_quantity=int(input("Enter Product quantity : "))
            product_price=int(input("Enter Product Price : "))
            vendar_name=input("Enter Vendor Name : ")
            
            my_company_obj.sales_data[product_name]['product_quantity']+=product_quantity
            my_company_obj.sales_data[product_name]['product_price']+=product_price
            my_company_obj.sales_data[product_name]['sales_number']='SO/'+'0000'+str(my_company_obj.sales_no)
                
            my_company_obj.sales_no +=1
            
            my_company_obj.purchase_data[product_name]['product_quantity'] -=product_quantity
            unit_price=my_company_obj.purchase_data[product_name]['unit_price']
                
            my_company_obj.purchase_data[product_name]['product_price'] -=int(product_quantity*unit_price)
                
    ###########################################################################################################
    
    def create_manufacture_order(self):
        
        '''
            func   :- it is used manufacture product

        '''
        
        product_name=input("Enter Product Name for Manufacture  : ")
        date=datetime.datetime.today().strftime('Date : %d-%m-%Y Time : %H:%M:%S')
        
        if product_name in my_company_obj.raw_matirial_data.keys():
            my_company_obj.manufacture_order(product_name)
            product_quantity=int(input("Enter Product quantity For Manufacture : "))
            
            raw_material_qty=my_company_obj.raw_matirial_data[product_name]['product_quantity']
            
            if product_quantity > raw_material_qty:
                
                print("\nNo Enough Quantity Available Right Now... \n")
                
            else:
                
                my_company_obj.manufacture_data[product_name]={'product_name':product_name}
                my_company_obj.manufacture_data[product_name]['product_quantity']=product_quantity
                my_company_obj.manufacture_data[product_name]['manufacture_date']=date
                my_company_obj.manufacture_data[product_name]['manufacture_number']='MO/'+'0000'+str(my_company_obj.manufacture_no)
                
                print("Product Manufacture Successfully...\n")
                print(my_company_obj.done_manufacture(product_name))
                product_price=int(input("Enter New Manufacture Product Price : "))
                
                # storing data on purchase data
                
                print("New Product Now Available in Stock Now...\n")
                
                unit_price=product_price / product_quantity
                
                my_company_obj.purchase_data[product_name]={'product_name':product_name}
                my_company_obj.purchase_data[product_name]['product_type']=product_type
                my_company_obj.purchase_data[product_name]['product_quantity']=product_quantity
                my_company_obj.purchase_data[product_name]['product_price']=product_price
                my_company_obj.purchase_data[product_name]['unit_price']=unit_price
                my_company_obj.purchase_data[product_name]['product_date']=date
                my_company_obj.purchase_data[product_name]['purchase_number']='PO/'+'0000'+str(my_company_obj.purchase_no)
                
        else:
            print("Entered Raw Material is Not Available")
            
    #############################################################################################################
    
     
    
    #############################################################################################################
my_company_obj=my_company()

choice=1
while(choice>0 and choice<11):
        print("\n 1 Company_information \n 2 Purchase \n 3 Sales \n 4 Stock \n 5 Manufacture \n 6 Purchase Raw Material \n 7 Sales Record \n 8 Raw Material Record \n 10 Exit")
        choice=int(input("\nEnter your choice: \n"))
        if choice==1:
            
            my_company_obj.Company_info()
            
        elif choice==2:
            print("Purchase")
            my_company_obj.create_purchase_order()
            
        elif choice==3:
            print("Sales")
            
            my_company_obj.create_sales_order()
        
        elif choice==4:
            print("Stock Details")
            for i in my_company_obj.purchase_data.keys():
                print(my_company_obj.purchase_data[i])
                
        elif choice==5:
            
            print("Manufacture")
            my_company_obj.create_manufacture_order()
            
        elif choice==6:
        
            print("Purchase rawmaterial")
            product_name=input("Enter Product Raw Matirial's Name : ")
            product_type=input("Enter Product Type (Stock / Consumable) : ")
            product_quantity=int(input("Enter Product Quantity : "))
            product_price=int(input("Enter Raw Matirial's Product Price : "))
            per_product_price=product_price / product_quantity
            date=datetime.datetime.today().strftime('Date: %d/%m/%Y Time: %H:%M:%S')
            
            if not product_name in my_company_obj.raw_matirial_data.keys():
                
                my_company_obj.raw_matirial_data[product_name]={'product_name':product_name}
                my_company_obj.raw_matirial_data[product_name]['product_name']=product_name
                my_company_obj.raw_matirial_data[product_name]['product_type']=product_type
                my_company_obj.raw_matirial_data[product_name]['product_quantity']=product_quantity
                my_company_obj.raw_matirial_data[product_name]['product_price']=product_price
                my_company_obj.raw_matirial_data[product_name]['per_product_price']=per_product_price
                my_company_obj.raw_matirial_data[product_name]['date']=date
                my_company_obj.raw_matirial_data[product_name]['product_no']='PO/'+'0000'+str(my_company_obj.purchase_no)                
            else:
                
                my_company_obj.raw_matirial_data[product_name]['product_quantity'] += product_quantity
                my_company_obj.raw_matirial_data[product_name]['product_price'] +=product_price
                my_company_obj.raw_matirial_data[product_name]['per_product_price'] +=per_product_price
                my_company_obj.raw_matirial_data[product_name]['date']=date
                my_company_obj.raw_matirial_data[product_name]['product_no']='PO/'+'0000'+str(my_company_obj.purchase_no)
                
            my_company_obj.purchase_no +=1
            
            print("Raw Matirial's Purchase Successfully...")
            
        elif choice==7:
            
            print("sales data")
            for i in my_company_obj.sales_data:
                print(my_company_obj.sales_data[i])
                
        elif choice==8:
            
            print("Raw material")
            for i in my_company_obj.raw_matirial_data:
                print(my_company_obj.raw_matirial_data[i])
                   
        elif choice==10:
            exit()
        else:
            print("Invalid Choice")
        
        