{
    'name':'Employee Management',
    'category':'employee',
    'sequence':'1',
    'summary':'Employee Management ',
    'website':'http://www.emiprotechnologies.com/',
    'version':'1.0',
    'description':'This application is for Employee management',
    
    'depends':[
               'base',
               ],
    
    'data':[
            'security/ir.model.access.csv',
            'views/employee_ept_view.xml',
            ],
    'installable':True,
    'application':True,
    'auto-install':False,

}