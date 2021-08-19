# -*- coding: utf-8 -*-
from odoo import models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _prepare_invoice(self):
        """
        Agrega el campo client_order_ref a las referencias cruzadas de la factura
        """
        vals = super(SaleOrder, self)._prepare_invoice()
        if self.client_order_ref:
            vals["l10n_cl_reference_ids"] = [(0, 0, {
                "origin_doc_number": self.client_order_ref,
                "l10n_cl_reference_doc_type_selection": "801",
                "date": self.date_order
            })]
        return vals
