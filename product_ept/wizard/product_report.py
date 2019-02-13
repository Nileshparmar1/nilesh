from odoo import models, fields
import base64
from io import BytesIO
try:
    import xlwt
except ImportError:
    xlwt = None


class ProductReport(models.TransientModel):
    
    _name = 'product.report'
    
    datas = fields.Binary('File')
    product_category_id = fields.Many2one('product.ept.category', string="Product Category")
    
    def generate_report(self):

        workbook = xlwt.Workbook()
        worksheet = workbook.add_sheet('product report', cell_overwrite_ok=True)
        
        rows = 0
        header_list = ['name', 'price', 'description']
        for column, header in enumerate(header_list):
            worksheet.write(rows, column, header) 
            
        products = self.env['product.ept'].search([('product_ept_category_id', '=', self.product_category_id.id)])
        rows = 1
        for product in products:
            worksheet.write(rows, 0, product.name)
            worksheet.write(rows, 1, product.price)
            worksheet.write(rows, 2, product.description)
            rows += 1
                  
        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        report_file = base64.encodestring(fp.read())
        fp.close()
        
        self.write({'datas':report_file, 'file_name':'product report'})
        return{
            'type':'ir.actions.act_url',
            'url': 'web/content/?model=product.report&field=datas&download=true&id=%s&filename=product_category_report.xls' % (self.id),
            'target':'self',
            }
        
                       
