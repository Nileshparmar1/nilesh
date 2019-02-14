from odoo import models,fields,api,tools

class SaleReportEpt(models.Model):
    
    _name='sale.report.ept'
    _auto=False
    
    confirmation_date = fields.Datetime(string='Confirmation Date',readonly=True)
    amount_total = fields.Float(string="Total",readonly=True)                                    
    
    def _select(self):
        return"""
            SELECT 
                id,s.confirmation_date,
                s.amount_total
            """

    def _from(self):
        return"""
            FROM sale_order_ept AS s
            """

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, self._table)
        self._cr.execute("""
            CREATE OR REPLACE VIEW %s AS (
                %s
                %s
            )
        """ % (self._table, self._select(), self._from())
        )
        
        