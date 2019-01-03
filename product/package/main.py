import re
from purchase import Purchase_product
class mycompany(Purchase_product):
    p=({})
    def create_purchase(self,id,name,price):
        p=mycompany_obj.purchase(id,name,price)
        return p
    
mycompany_obj=mycompany()
choice=1
id='po/0000'
while(choice):
    if(choice>0 and choice<5):
        print("1 Purchase 2 Sales 3 Stock 4 Exit")
        choice=int(input("Enter Your Choice: "))
        if choice==1:
            id=re.sub('\d(?!\d)',lambda x:str(int(x.group(0))+1),id)
            name=input("Enter Name: ")
            price=input("Enter Price: ")
            p=mycompany_obj.create_purchase(id,name,price)
            print(p)
            
        elif choice==2:
            print("sales")
            
        elif choice==3:
            print("stock")
            
               
        elif choice==4:
            exit()
        else:
            print("Invalid choice")
            
            
               


    