# -*- coding: utf-8 -*-
{
    'name': 'Tanax Reportes',
    'version': '0.4',
    'license': 'AGPL-3',
    'summary': 'Reporteria de tanax',
    'author': u'ERP Siglo 21',
    'depends': ['sale_management','l10n_cl_edi',],
    'data': [
        'security/ir.model.access.csv',
        'reports/delivery_guide_document.xml',
        'reports/leadtime.xml',
        'reports/report_invoice.xml',
        'reports/report_picking.xml',
        'reports/vtaprod.xml',
#        'wizards/manifiesto.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
