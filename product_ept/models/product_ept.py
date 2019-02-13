from odoo import models,fields,api
from odoo.exceptions import Warning

class ProductEpt(models.Model):
    
    _name='product.ept'
    
    @api.depends('price','on_hand_quantity')
    def _get_total_price(self):
        for i in self:
            i.total_price=i.price*i.on_hand_quantity
    
    name = fields.Char(string = "name",require = True,help="Product Name")
    product_ept_category_id=fields.Many2one('product.ept.category',string="Product Category",help="product category from product ept category")
    brand_id=fields.Many2one('product.brand.ept',string="Product Brand",help="product brand from product brand ept model")
    active = fields.Boolean(string = "Active", default=True)
    type = fields.Selection([('stockable', 'Stockable'), ('consumable', 'Consumable'), ('service', 'Service')],default='stockable',required=True,help="Product Type")    
    price = fields.Float(string = "price",help="Product Price")    
    on_hand_quantity = fields.Integer(string = "quantity",help="Available Quantity") 
    description = fields.Html(string = "Description",help="Product Description")
    barcode = fields.Char(string = "Barcode",help="product Barcode No")   
    image = fields.Binary(string = "product Image",help="Upload Product Image")
    date = fields.Date(string = "Date",help="Product Purchase Date")
    issale = fields.Boolean(string = "salable",help="Product is salable or not")
    total_price = fields.Float(string = 'Total Price', compute = '_get_total_price',help="Total Price of Product")
    inherit_id = fields.Reference(string="Reference",selection=[('product.brand.ept', 'Brand Name'), ('product.ept.category', 'Category Name')])
    
    @api.model
    def create(self, values):
        
        ''' This function is used to create a product '''
        res = super(ProductEpt, self).create(values)
        return res
    
    @api.multi
    def write(self, values):

        return super(ProductEpt, self).write(values)
    
    @api.multi
    def unlink(self):
    
        if self.issale:
            raise Warning("Salable Product Can't Delete")
        else:
            return super(ProductEpt, self).unlink()
    
        
    @api.constrains('on_hand_quantity')
    def quantity_constraint(self):
        
        ''' @func: this function constrain on on_hand_quantity not less than 1. '''
        
        if self.on_hand_quantity < 0 :
            raise Warning("Please Enter Quantity")
    
    
    
    