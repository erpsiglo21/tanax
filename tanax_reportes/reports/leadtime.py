# -*- coding: utf-8 -*-
from odoo import tools
from odoo import fields, models


class LeadTime(models.Model):
    _name = "tanax.leadtime"
    _description = "Reporte leadtime"
    _auto = False
    _rec_name = 'id'

    partner_vat = fields.Char('RUT', readonly=True)
    partner_name = fields.Char('Cliente', readonly=True)
    partner_address = fields.Char('Direccion despacho', readonly=True)
    sale_order = fields.Char('Orden de venta', readonly=True)
    order_date = fields.Date('Fecha OV', readonly=True)
    invoice = fields.Char('Factura', readonly=True)
    invoice_date = fields.Date('Fecha Factura', readonly=True)
    invoice_date_due = fields.Date('Fecha Vcto Factura', readonly=True)
    delivery = fields.Char('Despacho', readonly=True)
    delivery_date = fields.Date('Fecha Despacho', readonly=True)
    fecha_agendamiento = fields.Date('Fecha Agendamiento', readonly=True)
    fecha_camion = fields.Date('Fecha Salida', readonly=True)
    fecha_entrega = fields.Date('Fecha Entrega', readonly=True)


    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table,"""
select distinct
       row_number() over() as id
      ,rp.vat as partner_vat
      ,rp.name as partner_name
      ,trim(rps.street) || ', ' || trim(rps.city) as partner_address
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
       inner join res_partner rp
          on rp.id = so.partner_id
       inner join res_partner rps
	      on rps.id = so.partner_shipping_id
       inner join stock_picking sp
          on sp.id = sm.picking_id
       inner join sale_order_line_invoice_rel soin
          on soin.order_line_id = sol.id
       inner join account_move_line aml
          on aml.id = soin.invoice_line_id
       inner join account_move am
          on am.id = aml.move_id
         and am.state = 'posted'
  where sm.picking_type_id in (select id
                                 from stock_picking_type
                                where code = 'outgoing')
         """))