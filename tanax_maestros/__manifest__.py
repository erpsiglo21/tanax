# -*- coding: utf-8 -*-
{
    'name': 'Tanax Maestros',
    'version': '0.2',
    'license': 'AGPL-3',
    'summary': 'Agrega informacion necesaria en los maestros',
    'author': u'ERP Siglo 21',
    'depends': ['base'],
    'data': [
        "security/ir.model.access.csv",
        "security/security.xml",
        'views/res_canal_views.xml',
        'views/res_partner_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}