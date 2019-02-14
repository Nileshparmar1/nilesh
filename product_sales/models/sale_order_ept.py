from odoo import models, fields, api, _


class saleorderept(models.Model):
    _name = 'sale.order.ept'
    _description = 'sale order ept'
    _rec_name = 'partner_id'
   
    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
            order.update({
                'amount_total': amount_untaxed
            })
    
    name = fields.Char(string='Order Reference', required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    partner_id = fields.Many2one('partner.ept', string="Customer Name", help="Partner name")
    date = fields.Date(string="Validity", help="Validity date of the quotation, after this date, the customer won't be able to validate the quotation online.")
    confirmation_date = fields.Datetime(string='Confirmation Date', readonly=True, index=True, help="Date on which the sales order is confirmed.")
    order_line = fields.One2many('sale.order.line.ept', 'order_id', string='Order Lines', copy=True, auto_join=True)
    amount_total = fields.Float(string="Total", compute='_amount_all', store=True, readonly=True)
    
    state = fields.Selection([
        ('draft', 'Quotation'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')
    
    @api.multi
    def write(self, values):
        
        return super(saleorderept, self).write(values)
    
    @api.multi
    def unlink(self):
        
        return super(saleorderept, self).unlink()
        
    @api.multi
    def action_confirm(self):
        
        return self.write({
            'state':'sale',
            'confirmation_date':fields.Datetime.now()
            })
        
    @api.multi
    def action_cancel(self):
        
        return self.write({'state':'cancel'})
    
    @api.multi
    def action_quotation(self):
        
        return self.write({'state':'draft'})
    
    @api.multi
    def action_done(self):
    
        return self.write({'state':'done'})
    
    @api.multi
    def action_unlock(self):
        
        return self.write({'state':'sale'})
    
    @api.model
    def create(self, vals):
        '''
        @func: this function is used to create sale order no.
        '''
        if vals.get('name', _('New')) == _('New'):
            if 'company_id' in vals:
                vals['name'] = self.env['ir.sequence'].with_context(force_company=vals['company_id']).next_by_code('sale.order.ept') or _('New')
            else:
                vals['name'] = self.env['ir.sequence'].next_by_code('sale.order.ept') or _('New')
        return super(saleorderept, self).create(vals)

    @api.multi
    def print_saleorder(self):
        ''' This method for print order '''
        return self.env.ref('product_sales.action_report_saleorder')\
            .with_context({'discard_logo_check': True}).report_action(self)
        
class saleorderline(models.Model):
    
    ''' this class is used to create a sale order line in sale order. '''
    
    _name = 'sale.order.line.ept'
    _description = 'sale order line ept'
    
    @api.depends('price_unit', 'product_uom_qty')
    def _compute_amount(self):
        """
        @func: Compute the amounts of the SO line.
        """
        for line in self:
            
            line.update({'price_subtotal':line.price_unit * line.product_uom_qty})    
    
    order_id = fields.Many2one('sale.order.ept', string='Order Reference', required=True)
    product_id = fields.Many2one('create.product.ept', string='Product')
    product_uom_qty = fields.Float(string='Ordered Quantity', required=True, default=1.0)
    price_unit = fields.Float('price', required=True)
    price_subtotal = fields.Float('Subtotal', compute='_compute_amount', readonly=True, store=True)
    price_total = fields.Float('Subtotal', compute='_compute_amount', readonly=True, store=True)
    
    @api.multi
    @api.onchange('product_id')
    def onchange_product_price(self):
        
        '''
        @func: this method is used for get product price when product selected in sale order line.
        '''
        
        product_id = self.env['create.product.ept'].search([('id', '=', self.product_id.id)])
        self.update({'price_unit':product_id.price})
    
