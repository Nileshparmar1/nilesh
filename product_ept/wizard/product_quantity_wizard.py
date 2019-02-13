from odoo import models, fields,api

class ProductQuantity(models.TransientModel):
    
    _name='product.quantity.wizard'

    quantity=fields.Integer(string='Quantity')

    @api.multi
    def update_quantity(self):
        context = dict(self._context) or {}
        id = self.env['product.ept'].browse(context.get('active_id', False))
        id.update({'on_hand_quantity':self.quantity})
        
        
        
        
        