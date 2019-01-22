from odoo import models,fields
class partner(models.Model):
    _name='partner.ept'
    _description='partner ept'
    
    image=fields.Binary(string="Customer Image",help="partner image")
    name=fields.Char(string="Name",require=True,help="Partner Name")
    city=fields.Char(string="City",help="Partner City")
    state=fields.Char(string="State",help="Partner State")
    mobile_no=fields.Char(string="Mobile No",help="Partner Mobile no")