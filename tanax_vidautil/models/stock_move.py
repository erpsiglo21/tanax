# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockMove(models.Model):
    _inherit = 'stock.move'

    def _action_assign(self):
        for record in self:
            result = super(StockMove, self)._action_assign()
            move_line_under_ids = record.move_line_ids.filtered(lambda l: l.is_under_customer_percentage)
            move_line_over_ids = record.move_line_ids.filtered(lambda l: not l.is_under_customer_percentage)
            move_line_under_ids.write({'is_under_percentage': True})
            move_line_over_ids.write({'is_under_percentage': False})
            return result
