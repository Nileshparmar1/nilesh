from odoo import models,fields,api


class Lead(models.Model):
    _inherit = 'crm.lead'

    @api.multi
    def change_priority(self):
        print("hello")
        print(fields.Date.today())
        records = self.env['crm.lead'].search([('date_deadline','<',fields.Date.today())])
        for record in records:
            record.priority='3'
            
        
        
        
        
            
    