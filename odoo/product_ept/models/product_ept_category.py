from odoo import models,fields

class ProductEptCategory(models.Model):
    _name='product.ept.category'
    
    name = fields.Char(string="Name",require=True)
    description=fields.Html(string="Description")
    no_of_brand = fields.Char(string="No of Brand")
    no_of_available_product=fields.Integer(string="No of available product")
    
    
    
    