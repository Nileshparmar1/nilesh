from odoo import fields, models, api


class ChangeQuantity(models.TransientModel):
    
    _name = 'change.quantity.wizard'

    '''
    @api.multi
    def _default_product_name(self):
        context = dict(self._context) or {}
        product_id = self.env['create.product.ept'].browse(context.get('active_id', False))
        return product_id and product_id.id or False
    '''

    @api.model
    def default_get(self, fields_list):
        ''' this method used to set default product name '''
        res = super(ChangeQuantity, self).default_get(fields_list)
        # product_id=self._context.get('active_id',False)
        # res.update({'product_ept_id':product_id})
        res.update({'product_ept_id':self._context.get('active_id', False)})
        return res
    
    product_ept_id = fields.Many2one('create.product.ept', string="Name", readonly=True)
    
    # product_ept_id = fields.Char(string="Name")
    quantity = fields.Float(string="New Quantity", help="Quantity")
                
    @api.multi
    def update_quantity(self):
        
        context = dict(self._context) or {}
        product_id = self.env['create.product.ept'].browse(context.get('active_id', False))
        product_id.update({'on_hand_quantity':product_id.on_hand_quantity + self.quantity})

