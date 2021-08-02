# -*- coding: utf-8 -*-
from odoo import api, models, fields, _

class Partner(models.Model):
    _inherit = "res.partner"

    canal_id = fields.Many2one('res.canal')
    codigo_interno = fields.Integer(string="Codigo interno")
    exigencia = fields.Integer(string="Porcentaje de exigencia")
