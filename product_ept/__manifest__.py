{
    'name':'Product_Ept',
    
    'version':'1.0',
     
    'category':'product',
    
    'sequence':2,
    
    'summary':'product details ',
    
    'website':'www.emoprotechnologies.com',
    
    'author':'Nilesh Parmar',
    
    'depends':['base'],
    
    'data':['security/ir.model.access.csv',
            'views/product_view.xml',
            'views/product_category_view.xml',
            'wizard/product_report_view.xml',
            'wizard/product_quantity_view.xml'
            ],
    
    'installable':True,
    
    'auto_install':False,
    
    'application': True

}