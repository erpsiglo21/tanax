# -*- coding: utf-8 -*-
from odoo import tools
from odoo import fields, models


class LeadTime(models.Model):
    _name = "tanax.leadtime"
    _description = "Reporte leadtime"
    _auto = False
    _rec_name = 'id'

    sale_order = fields.Char('Orden de venta', readonly=True)
    order_date = fields.Datetime('Fecha OV', readonly=True)
    invoice = fields.Char('Factura', readonly=True)
    invoice_date = fields.Datetime('Fecha Factura', readonly=True)
    invoice_date_due = fields.Datetime('Fecha Vcto Factura', readonly=True)
    delivery = fields.Char('Despacho', readonly=True)
    delivery_date = fields.Datetime('Fecha Despacho', readonly=True)
    fecha_agendamiento = fields.Datetime('Fecha Agendamiento', readonly=True)
    fecha_camion = fields.Datetime('Fecha Salida', readonly=True)
    fecha_entrega = fields.Datetime('Fecha Entrega', readonly=True)


    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table,"""
select distinct
       row_number() over() as id
      ,so.name as sale_order
      ,so.create_date order_date
      ,am.name as invoice
      ,am.invoice_date as invoice_date
      ,am.invoice_date_due as invoice_date_due
      ,sp.name as delivery
      ,sp.date_done as delivery_date
      ,sp.fecha_agendamiento as fecha_agendamiento
      ,sp.fecha_camion as fecha_camion
      ,sp.fecha_entrega as fecha_entrega
  from stock_move sm
       inner join sale_order_line sol
          on sol.id = sm.sale_line_id
       inner join sale_order so
          on so.id = sol.order_id
       inner join stock_picking sp
          on sp.id = sm.picking_id
       inner join sale_order_line_invoice_rel soin
          on soin.order_line_id = sol.id
       inner join account_move_line aml
          on aml.id = invoice_line_id
       inner join account_move am
          on am.id = aml.move_id
  where sm.picking_type_id in (select id
                                 from stock_picking_type
                                where code = 'outgoing')
         """))