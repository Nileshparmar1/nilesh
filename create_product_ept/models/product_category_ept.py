from odoo import models,fields,api

class ProductEptCategory(models.Model):
    _name='product.category.ept'
    @api.multi
    def product_count(self):
        count=self.mapped('product_ept_ids')
        self.count=len(count)
        
    @api.multi
    def view_product(self):
        products = self.mapped('product_ept_ids')
        action = self.env.ref('create_product_ept.product_ept_action').read()[0]
        if len(products) > 1:
            action['domain'] = [('id', 'in', products.ids)]
        elif len(products) == 1:
            action['views'] = [(self.env.ref('create_product_ept.product_ept_view_form').id,'form')]
            action['res_id'] = products.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action   
    
    name = fields.Char(string="Name",require=True,help="Category Name")
    product_ept_ids = fields.One2many('create.product.ept','product_ept_category_id',string="Product Name",help="Products from product ept")
    description = fields.Html(string="Description",help="Category Description")
    no_of_brand = fields.Char(string="No of Brand",help="No of Brand")
    count=fields.Integer(string="count",compute="product_count",readonly=True,help="Count No of Product")
    type = fields.Selection([('stockable', 'Stockable'), ('consumable', 'Consumable'), ('service', 'Service')],help="Product Type")
    