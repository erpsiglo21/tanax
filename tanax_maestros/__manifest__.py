# -*- coding: utf-8 -*-
{
    'name': 'Tanax Maestros',
    'version': '0.5',
    'license': 'AGPL-3',
    'summary': 'Agrega informacion necesaria en los maestros',
    'author': u'ERP Siglo 21',
    'depends': ['base','contacts','stock','sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_template_views.xml',
        'views/res_canal_views.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
        'views/stock_picking_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}