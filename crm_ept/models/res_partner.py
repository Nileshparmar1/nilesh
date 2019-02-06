from odoo import fields,models,api

class ResPartner(models.Model):
    
    _name='crm.partner.ept'
    _description='crm partner ept'
    
    
    name=fields.Char(string="Name",help="Customer Name")
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    
    '''
    @api.onchange('state_id')
    def _onchange_state(self):
        if self.state_id:
            self.country_id = self.state_id.country_id.id
    '''
    
    @api.onchange('country_id')
    def _onchange_country(self):
        '''This func is used for get state name on change country name'''
        state_list={}
        #self.state_id.country_id.ids=self.country_id
        state_list['domain'] = {'state_id':[('country_id','=',self.country_id.id)]}
        return state_list
              
        
    