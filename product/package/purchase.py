
class Purchase_product:
    dict=({})
    def purchase(self,id,name,price):
        self.dict.update({'id':id,'name':name,'price':price})
        
        return self.dict
        
        