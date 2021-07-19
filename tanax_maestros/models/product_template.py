# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    codigo_barra = fields.Char(string="Codigo EAN/DUN", size=20)
    #unidades_caja = fields.Integer(string="Unidades por caja", default=1)
