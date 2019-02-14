{
    'name':'Product Sale',
    'version':'12.0.1.0',
    'category':'Sales',
    'summary':'Sales Product',
    'description':""" 
this module contain all feature of sales management and e-commerce
""",
    'website':'www.emoprotechnologies.com',
    'author':'Nilesh Parmar',
    'depends':['base'],
    'data':['security/ir.model.access.csv',
            'views/partner_view.xml',
            'views/sale_order_view.xml',
            'data/ir_sequence_data.xml',
            'data/report_paperformat.xml',
            'report/sale_report.xml',
            'report/sale_template.xml',
            'report/sale_activity_report_views.xml'
            ],
    'installable':True,
    'application':True,
    'auto_install':False,
}