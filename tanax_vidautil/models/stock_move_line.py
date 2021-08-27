# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime, timedelta


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    requirement_percentage = fields.Float(string='Porcentaje de VU',
                                          compute='_compute_requirement_percentage')
    is_under_customer_percentage = fields.Boolean(string='Por debajo del porcentaje requerido',
                                                  compute='_compute_requirement_percentage')
    is_under_percentage = fields.Boolean(string='Por debajo del porcentaje requerido',
                                         default=False)
    production_days = fields.Float(compute='_compute_requirement_percentage')
    days_today = fields.Float(compute='_compute_requirement_percentage')
    # production_date = fields.Date(string='Fecha de fabricación',
    #                               default=datetime.strptime('%s-01-01' % (fields.Date.today().year), "%Y-%m-%d").date())
    production_date = fields.Date(string='Fecha de fabricación',
                                  default=lambda self: fields.Date.context_today(self))

    @api.depends('picking_id.partner_id', 'product_id',
                 'lot_id', 'lot_id.expiration_date',
                 'lot_id.production_date', 'picking_id.partner_id.exigencia')
    def _compute_requirement_percentage(self):
        for record in self:
            requirement_percentage = 100
            product_expiration_date = record.lot_id.expiration_date
            product_production_date = record.lot_id.production_date or datetime.strptime('%s-01-01' % (fields.Date.today().year), "%Y-%m-%d").date()
            days_today = 0
            production_days = 0
            if product_expiration_date:
                days_today = (product_expiration_date.date() - fields.Date.today()).days
                production_days = (product_expiration_date.date() - product_production_date).days
            record.days_today = days_today
            record.production_days = production_days
            if production_days:
                requirement_percentage = (1 - (production_days - days_today) / production_days) * 100
            record.requirement_percentage = requirement_percentage
            exigencia = record.picking_id.partner_id.exigencia
            is_under_customer_percentage = False
            if exigencia:
                is_under_customer_percentage = exigencia >= requirement_percentage
            record.is_under_customer_percentage = is_under_customer_percentage

    def _assign_production_lot(self, lot):
        super()._assign_production_lot(lot)
        self.lot_id._update_prod_date_values(self.production_date)

    @api.onchange('lot_id')
    def _onchange_lot_id(self):
        super(StockMoveLine, self)._onchange_lot_id()
        if not self.picking_type_use_existing_lots or not self.product_id.use_expiration_date:
            return
        if self.lot_id:
            self.production_date = self.lot_id.production_date
        else:
            self.production_date = False
