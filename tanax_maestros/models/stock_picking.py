# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class StockPicking(models.Model):
    _inherit = "stock.picking"

    fecha_agendamiento = fields.Datetime(
        'Fecha agendamiento', 
        help="Fecha de agendamiento")
    fecha_camion = fields.Datetime(
        'Fecha partida camion', 
        help="Fecha en que se inicio el despacho")
    fecha_entrega = fields.Datetime(
        'Fecha real de entrega', 
        help="Fecha en que se realizo la entrega al cliente")
