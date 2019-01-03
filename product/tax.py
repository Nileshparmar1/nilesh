class tax_calculate:
    def get_tax(self,price,product_type):
        print("tax")
        if type=='stock':
            cgst=price*10/100
            sgst=price*12/100
            total_tax=price+cgst+sgst
        else:
            total_tax=price*10/100
        return total_tax
    