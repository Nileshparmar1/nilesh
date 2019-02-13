from odoo import models, fields, api
from odoo.exceptions import Warning

class ProductEpt(models.Model):
    
    _name = 'create.product.ept'
    
    '''
    @api.depends('price','on_hand_quantity')
    def calculate_total_price(self):
        self.total_price=self.price*self.on_hand_quantity
    '''    
    name = fields.Char(string="name", require=True, help="Product Name")
    
    ''' Relation on product ept category to set the product category'''
    
    product_ept_category_id = fields.Many2one('product.category.ept', string="product_category", help="product category from product ept category")
    
    active = fields.Boolean(string="Active", default=True)
    type = fields.Selection([('stockable', 'Stockable'), ('consumable', 'Consumable'), ('service', 'Service')], required=True, help="Product Type")    
    price = fields.Float(string="price", help="Product Price")    
    on_hand_quantity = fields.Float(string="quantity", help="Available Quantity") 
    description = fields.Html(string="Description", help="Product Description")
    barcode = fields.Char(string="Barcode", help="product Barcode No")   
    image = fields.Binary(string="product Image", help="Upload Product Image")
    date = fields.Date(string="Date", help="Product Purchase Date")
    issale = fields.Boolean(string="salable", help="Product is salable or not")
    # total_price = fields.Float(string = "Total Price",compute='calculate_total_price',store=True,help="Total Price of Product")
    total_price = fields.Float(string="Total Price", help="Total Price of Product")
    product_brand = fields.Char(string="No of Brand", related='product_ept_category_id.no_of_brand', help="No of Brand")
    inherit_id = fields.Reference(string="Reference", selection=[('create.product.ept', 'Product Name'), ('product.category.ept', 'Category Name')])
    _sql_constraints = [
        ('product_barcode_unique', 'unique (barcode)', 'Product Barcode must be Unique !')]

    @api.onchange('price', 'on_hand_quantity', 'type')
    def _onchange_totalprice(self):
        
        '''
        @func:'this method is used for calculate total price'
        @param price:it's type Float
        @return: total price of product   
        
        '''
        result = {}
        if self.price < 0 :
            raise Warning(("Product Price should be minimum 100"))
        self.total_price = self.price * self.on_hand_quantity
        
        ''' result is used to get only same type product category '''  
        result['domain'] = {'product_ept_category_id':[('type', '=', self.type)]}
        return result
        
        '''
            it is used when change name of product type is display like product name
            result['domain'] = {'product_ept_category_id':[('name','ilike',self.name)]}
            return result
        '''
    
    @api.model
    def create(self, values):
        
        ''' This function is used to create a product '''
        res = super(ProductEpt, self).create(values)
        return res
    
    @api.multi
    def write(self, values):
        res = super(ProductEpt, self).write(values)
        #product_id = self.search([('price', '>', 200)], offset=0, limit=10, order='name', count=False)
        # product_id.name
        #for product in product_id:
        #    print(product.name)
            
        return res

    @api.multi
    def unlink(self):
        if self.issale != True :
            return super(ProductEpt, self).unlink()
        else:
            raise Warning("Salable Product Can't Delete")
        
    @api.constrains('on_hand_quantity')
    def quantity_constraint(self):
        '''
        @func: this finction constrain on on_hand_quantity not less than 1.
        '''
        if self.on_hand_quantity < 0 :
            raise Warning("Please Enter Quantity")
        
    @api.multi
    def action_update_quantity_on_hand(self):
        '''
        @func:'this method is used for update quantity'
        @param: 
        @return: updated product quantity 
        '''
        context = dict(self._context) or {}
        product_id = self.env['create.product.ept'].browse(self.id)
        context.update({'default_quantity':product_id.on_hand_quantity})
        return {
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'change.quantity.wizard',
            'views':[[self.env.ref('create_product_ept.quantity_update_wizard_form').id, 'form']],
            'context':context,
            'target': 'new',
        }
              
    '''        
    @api.model
    def search_product(self, args, offset=0, limit=None, order=None, count=False):
        args=self.search([('price','>',200)])
        #product_id=self.search([('price','>',200)],offset=0,limit=None, order=False, count=False)
        return super(ProductEpt,self).search_product(args, offset, limit, order, count=count)
    
    '''
    
