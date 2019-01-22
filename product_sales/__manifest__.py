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
    'data':['views/partner_view.xml',
            'views/sale_order_view.xml',
            'security/ir.model.access.csv'
            ],
    'installable':True,
    'application':True,
    'auto_install':False,
}