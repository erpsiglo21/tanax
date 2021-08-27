# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vu_state = fields.Selection(selection=[('no_vu', 'No cumple VU'),
                                           ('vu', 'Cumple con Vu')],
                                compute='_compute_vu_state',
                                search='_search_vu_state',
                                string='Estado VU')

    @api.depends('move_lines', 'move_line_ids')
    def _compute_vu_state(self):
        for record in self:
            vu_state = (any(l.is_under_percentage for l in record.move_line_ids) and
                        'no_vu' or 'vu')
            record.vu_state = vu_state

    @api.model
    def _search_vu_state(self, operator, operand):
        picking_ids = self.env['stock.picking'].search([('id', operator, False)])
        if isinstance(operand, bool):
            pass
        else:
            if operator == ('==', '=') and operand == 'no_vu':
                operand = True
            elif operator == '!=' and operand == 'vu':
                operand = False
            elif operator in ('==', '=') and operand == 'vu':
                operand = False
            elif operator == '!=' and operand == 'no_vu':
                operand = True
            move_lines = self.env.get('stock.move.line').search([
                ('is_under_percentage', operator, operand)])
            picking_ids = move_lines.mapped('picking_id')
        return [('id', 'in', picking_ids.ids)]
