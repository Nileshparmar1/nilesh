from odoo import models,fields,api

class ProductEptCategory(models.Model):
    
    _name='product.ept.category'
    @api.multi
    def product_count(self):
        
        '''This method for count no of product '''
        count=self.mapped('product_ept_ids')
        self.count=len(count)
        
    @api.multi
    def view_product(self):
        
        ''' This method used for get no of product in form or tree view on base of no of product available. ''' 
        products = self.mapped('product_ept_ids')
        action = self.env.ref('product_ept.product_ept_data_action').read()[0]
        if len(products) > 1:
            action['domain'] = [('id', 'in', products.ids)]
        elif len(products) == 1:
            action['views'] = [(self.env.ref('product_ept.product_ept_view_form').id,'form')]
            action['res_id'] = products.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action 
    
        '''
        action_rec = self.env['ir.model.data'].xmlid_to_object('product_ept.product_ept_data_action')
        if action_rec:
            action = action_rec.read([])[0]
            return action
        '''  
      
    name = fields.Char(string="Name",require=True,help="Category Name")
    product_ept_ids = fields.One2many('product.ept','product_ept_category_id',string="Product Name",help="Products from product ept")
    description = fields.Html(string="Description",help="Category Description")
    no_of_brand = fields.Char(string="No of Brand",help="No of Brand")
    count=fields.Integer(string="count",compute="product_count",readonly=True,help="Count No of Product")
    
    @api.model
    def create(self, values):
        
        ''' This function is used to create a product category'''
        res = super(ProductEptCategory,self).create(values)
        return res
    
    @api.multi
    def write(self, values):
        
        return super(ProductEptCategory, self).write(values)

    @api.multi
    def unlink(self):
        return super(ProductEptCategory, self).unlink()
