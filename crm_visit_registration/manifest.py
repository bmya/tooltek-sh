# -*- coding: utf-8 -*-
{
    'name': 'CRM Visit Registration',
    'version': '15.0.1.0.0',
    'category': 'CRM',
    'summary': 'Register visits to customers',
    'description': """
        This module allows your salespeople in the field to easily register their visits to customers. They can select the customer from a list of nearby customers using their phone's GPS, or search for the customer by name. The location where the visit was registered is automatically saved. Important fields include: customer, date/time (defaults to current time but can be changed), checkbox to indicate whether a sale was made during the visit, and a comments field. Compatibility with the Odoo Android app is ideal. 
    """,
    'author': 'Gunther Viertel',
    'website': 'https://www.serca.cl',
    'depends': ['base', 'crm'],
    'data': [
        'security/ir.model.access.csv',
        'views/crm_visit_views.xml',
        'views/templates.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}