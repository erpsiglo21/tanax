from odoo import _, api, fields, models

class Canal(models.Model):
    _name = "res.canal"
    _description = "Canal"
    _order = "name"

    name = fields.Char(required=True, translate=True)
    partner_ids = fields.One2Many('res.partner', 'canal_id',
                                   string="Direcciones de despacho",
                                   readonly="true",
                                   domain=([('type','=','delivery')]))
