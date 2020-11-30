# -*- coding: utf-8 -*-
{
    'name': "Rapitech HR Employee",

    'summary': """
    	Modificaciones HR Employee
    """,

    'description': """
        Actualizaciones HR
    """,

    'author': "Rapid Technoigies",
    'website': "www.rapi.tech",

    'category': 'Employee',
    'version': '0.3',

    'depends': ['base','hr'],

    'data': [
        'security/ir.model.access.csv',
        'views/hr_maestros_view.xml',
        'views/hr_employee_view.xml',
        'data/hr.document.type.csv',
        'data/hr.pension.fund.csv',
        'data/hr.type.employee.csv',
        'data/masters.xml',
    ],
}
