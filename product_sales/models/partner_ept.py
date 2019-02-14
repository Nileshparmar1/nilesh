from odoo import models,fields,api

class PartnerEpt(models.Model):

    _name='partner.ept'
    _description='partner ept'
    
    image=fields.Binary(string="Customer Image",help="partner image")
    name=fields.Char(string="Name",require=True,help="Partner Name")
    city=fields.Char(string="City",help="Partner City")
    state=fields.Char(string="State",help="Partner State")
    mobile_no=fields.Char(string="Mobile No",help="Partner Mobile no")
    
    @api.model
    def create(self, values):
        
        '''This function is used to create a product brand'''
        
        res = super(PartnerEpt, self).create(values)
        return res
    
    @api.multi
    def write(self, values):
        
        return super().write(values)
    
    @api.multi
    def unlink(self):
        
        return super(PartnerEpt, self).unlink()
