from odoo import models,fields

class saleorderept(models.Model):
    _name='sale.order.ept'
    _description='sale order ept'
    
    partner_name_m2m=fields.Many2many('partner.ept','partner_sale_order','partner_id','sale_order_id',string="Customer Name")
