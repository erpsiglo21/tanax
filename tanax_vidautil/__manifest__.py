# -*- coding: utf-8 -*-
{
    'name': "Tanax Vida util",

    'summary': """
        Establece expiración por lote y avisa según cliente sobre porcentaje de exigencia
        """,

    'description': """
        - Establece fecha de expiración por lote
        - Porcentage de Exigencia del cliente
        - Aviso de estado de expiración por lote en movimientos de almacén
    """,

    'author': "ERP Siglo 21",
    'website': "http://erpsliglo21.cl",

    'version': '1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'product_expiry', 'tanax_maestros'],

    # always loaded
    'data': [
        'views/stock_production_lot_views.xml',
        'views/stock_move_views.xml',
        'views/stock_picking_views.xml',
    ],
}
