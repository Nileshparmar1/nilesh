{
    'name':'CRM Ept',
    
    'version':'12.0.1.0',
    
    'category':'product',
    
    'sequence':3,
    
    'summary':'Customers Information',
    
    'web':'www.emiprotechnologies.com',
    
    'data':[
        'views/res_partner_view.xml',
        'security/ir.model.access.csv',
        'data/crm_lead_cron.xml'
        ],
    
    'depends':['crm'],
    
    'installable':True,
    
    'auto_install':False,
    
    'application':True,
    
}