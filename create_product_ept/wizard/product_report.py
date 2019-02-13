from odoo import fields,models,api
from odoo.exceptions import  UserError
import base64
from io import BytesIO
try:
    import xlwt
    from xlwt import Borders
except ImportError:
    xlwt = None

class ProductReport(models.TransientModel):
    _name='product.report.ept'

    category_id = fields.Many2one('product.category.ept',string="Category")
    datas = fields.Binary('File')

    def generate_report(self):
        
        ''' func: This method is used for to generate report. '''

        workbook,category_name,sheet_name=self.add_heading()
        #self.prepare_data()

        products_obj = self.env['create.product.ept']
        products = []

        if self.category_id.name == 'wood':
            report = products_obj.search([('product_ept_category_id', '=', self.category_id.id)])
            products = list(report)
            row = 1
            column = 0
            for i in range(0,len(products)):
                name = products[i].name
                price = products[i].price
                qty = products[i].on_hand_quantity
                sheet_name.write(row, 0, name)
                sheet_name.write(row, 1, price)
                sheet_name.write(row, 2, qty)
                row+=1
                
        if self.category_id.name =='steel and wood':
            report = products_obj.search([('product_ept_category_id','=',self.category_id.id)])
            products = list(report)
            row = 1
            column = 0
            for i in range(0, len(products)):
                name = products[i].name
                price = products[i].price
                qty = products[i].on_hand_quantity
                sheet_name.write(row, 0, name)
                sheet_name.write(row, 1, price)
                sheet_name.write(row, 2, qty)
                row+=1
        elif self.category_id.name =='':
            raise UserError(('Category not found'))

        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        result_report = base64.encodestring(fp.read())
        fp.close()
        self.write({'datas': result_report, 'file_name': 'product_report.xls'})

        return {
            'type': 'ir.actions.act_url',
            'url': 'web/content/?model=product.report.ept&field=datas&download=true&id=%s&filename=product_report.xls' % (self.id),
            'target': self
        }

    def add_heading(self):

        workbook = xlwt.Workbook()
        row = 0
        category_name = self.category_id.name
        sheet_name = workbook.add_sheet('%s' % (category_name),cell_overwrite_ok=True)
        sheet_name.write(row, 0, 'Product Name')
        sheet_name.write(row, 1, 'price')
        sheet_name.write(row, 2, 'On Hand Quantity')

        sheet_name.col(0).width = 256 * 45
        sheet_name.col(2).width = 256 * 45

        return workbook,category_name,sheet_name






