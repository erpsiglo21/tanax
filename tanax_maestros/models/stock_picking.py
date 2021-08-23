# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class StockPicking(models.Model):
    _inherit = "stock.picking"

    client_order_ref = fields.Char('OC Cliente', compute='_compute_oc_cliente_factura', store=False)
    invoice_number = fields.Char('Factura', compute='_compute_oc_cliente_factura', store=False)

    fecha_agendamiento = fields.Date(
        'Fecha agendamiento', 
        help="Fecha de agendamiento")
    fecha_camion = fields.Date(
        'Fecha partida camion', 
        help="Fecha en que se inicio el despacho")
    fecha_entrega = fields.Date(
        'Fecha real de entrega', 
        help="Fecha en que se realizo la entrega al cliente")

    @api.depends('sale_id')
    def _compute_oc_cliente_factura(self):
        for picking in self:
            picking.client_order_ref = None
            picking.invoice_number = None
            if picking.sale_id:
                picking.client_order_ref = picking.sale_id.client_order_ref
                invoices = picking.sale_id.invoice_ids.filtered(lambda inv: inv.state == 'posted' and inv.move_type == 'out_invoice')
                if invoices:
                    picking.invoice_number = invoices[0].name
