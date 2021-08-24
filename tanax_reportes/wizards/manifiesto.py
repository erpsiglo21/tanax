# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class ManifiestoWizard(models.TransientModel):
    _name = "tanax.manifiesto.wizard"
    _description = "Manifiesto Wizard"

    partner_id = fields.Many2one("res.partner", string='Transportista', required=True)
    manifest_date = fields.Date('Fecha de salida', required=True)

    def action_confirm(self):
        return 