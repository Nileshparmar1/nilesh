#@PydevCodeAnalysisIgnore
from odoo import api , models , fields

class EmployeeEpt(models.Model):
    
    _name="employee.ept"
    _description="Employee EPT "
    
    name = fields.Char(string = "Employee Name " , required=True)
    city = fields.Char(string = "Employee City " , required=True)
    
    post = fields.Char(string = "Employee Job Possition " , required=True)
    
     
    
    