{
    'name':'Create Product',
    'version':'12.0.1.0',
    'category':'product',
    'sequence':4,
    'summary':'Create a new product in use of search,constraint,custom records rule,onchange',
    'web':'www.emiprotechnologies.com',
    'data':['views/create_product_ept_view.xml',
            'views/product_category_ept_view.xml',
            
            'wizard/change_quantity_wiz.xml',
            'wizard/product_report.xml',
            
            'security/ir.model.access.csv',
            'security/product_security.xml'
            ],
    'depends':['base'],
    'installcble':True,
    'auto_install':False,
    'application':True,
}