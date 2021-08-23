# -*- coding: utf-8 -*-
from odoo import tools
from odoo import fields, models


class VtaProd(models.Model):
    _name = "tanax.vtaprod"
    _description = "Reporte VtaProd"
    _auto = False
    _rec_name = 'id'

    tipo = fields.Char('TD', readonly=True)
    folio = fields.Integer('Numero documento', readonly=True)
    origen = fields.Integer('Numero referencia', readonly=True)
    fecha_emision = fields.Date('Fecha', readonly=True)
    partner_id = fields.Many2one('res.partner', 'Cliente', readonly=True)
    partner_name = fields.Char('Descripcion Cliente', readonly=True)
    cliente = fields.Integer('Codigo Cliente', readonly=True)
    direccion = fields.Char('Direccion ddespacho', readonly=True)
    canal = fields.Char('Canal', readonly=True)
    codigo = fields.Char('Codigo Producto', readonly=True)
    descripcion = fields.Char('Descripcion Producto', readonly=True)
    uom_id = fields.Many2one('uom.uom', 'UM', readonly=True)
    quantity = fields.Float('Cantidad', readonly=True)
    currency_id = fields.Many2one('res.currency', 'Moneda', readonly=True)
    price_unit = fields.Monetary('Precio', readonly=True)
    neto = fields.Monetary('Neto', readonly=True)


    def init(self):
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table,"""
select amvl.id as id
     ,amv.sequence_prefix as tipo
     ,amv.sequence_number as folio
	  ,amv.sequence_number as origen
	  ,amv.invoice_date    as fecha_emision
	  ,amv.partner_id      as partner_id
	  ,prn.name            as partner_name
	  ,shp.codigo_interno  as cliente
	  ,shp.name            as direccion
	  ,COALESCE(cnl.name, 'Sin canal') as canal
	  ,COALESCE(prd.default_code, tpl.default_code) as codigo
	  ,amvl.name           as descripcion
     ,amvl.product_uom_id as uom_id
	  ,amvl.quantity       as quantity
     ,amvl.currency_id    as currency_id
	  ,amvl.price_unit     as price_unit
	  ,amvl.price_subtotal as neto
  from account_move amv
       inner join account_move_line amvl
	      on amvl.move_id = amv.id
		 and amvl.exclude_from_invoice_tab = false
	    inner join res_partner prn
          on prn.id = amv.partner_id
       left join res_partner shp
         on shp.id = amv.partner_shipping_id
		  and shp.type = 'delivery'
	    left join res_canal cnl
	       on cnl.id = shp.canal_id
	    inner join product_product prd
	       on prd.id = amvl.product_id
	    inner join product_template tpl
	       on tpl.id = prd.product_tmpl_id
 where amv.move_type in ('out_invoice','out_refund')
   and amv.state = 'posted'
         """))