# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockProductionLot(models.Model):
    _inherit = 'stock.production.lot'

    production_date = fields.Date(string='Fecha de fabricación')

    def _update_prod_date_values(self, new_date):
        if new_date:
            self.write({'production_date': new_date})
