
from odoo import fields,models,api
class SaleOrder(models.Model):
    
    _inherit="sale.order"
    
    order_confirm_date=fields.Datetime(string="Order Confirm Date",readonly=True,help="Sale product confirmation date")
    
    @api.multi
    def action_confirm(self):
        '''
        this method inherit action_confirm from SaleOrder and set confirmation date 
        '''
        super(SaleOrder,self).action_confirm()
        self.write({
            'order_confirm_date': fields.Datetime.now()
        })
        return True