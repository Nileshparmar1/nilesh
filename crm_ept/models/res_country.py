from odoo import models, api
from odoo.addons.base.models.res_country import location_name_search


class Country(models.Model):
    
    _inherit = 'res.country'
        
    @api.multi
    @api.depends('name', 'code')
    def name_get(self):
        result = []
        for country in self:
            name = country.code + ' - ' + country.name
            result.append((country.id, name))
        return result        
            
    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args + []
        if name:
            domain = ['|', ('code', operator, name), ('name', operator, name)]
        country_ids = self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
        return self.browse(country_ids).name_get()

