# -*- coding: utf-8 -*-
{
    'name': 'Tanax Reportes',
    'version': '0.2',
    'license': 'AGPL-3',
    'summary': 'Reporteria de tanax',
    'author': u'ERP Siglo 21',
    'depends': ['sale_management','l10n_cl_edi',],
    'data': [
        'security/ir.model.access.csv',
        'reports/report_invoice.xml',
        'reports/vtaprod.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
