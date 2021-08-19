# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class StockPicking(models.Model):
    _inherit = "stock.picking"

    client_order_ref = fields.Char('OC Cliente', compute='_compute_oc_cliente', store=False)

    fecha_agendamiento = fields.Datetime(
        'Fecha agendamiento', 
        help="Fecha de agendamiento")
    fecha_camion = fields.Datetime(
        'Fecha partida camion', 
        help="Fecha en que se inicio el despacho")
    fecha_entrega = fields.Datetime(
        'Fecha real de entrega', 
        help="Fecha en que se realizo la entrega al cliente")

    @api.depends('sale_id')
    def _compute_oc_cliente(self):
        for picking in self:
            if picking.sale_id:
                picking.client_order_ref = picking.sale_id.client_order_ref
