# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def _prepare_purchase_order_line_data(
        self, so_line, date_order, purchase_id, company
    ):
        res = super(SaleOrder, self)._prepare_purchase_order_line_data(
            so_line, date_order, purchase_id, company
        )
        if so_line.customer_id and so_line.provider_id and\
                so_line.analytic_tag_ids:
            res.update({
                'customer_id': so_line.customer_id.id,
                'provider_id': so_line.provider_id.id,
                'analytic_tag_ids': [(6, 0, so_line.analytic_tag_ids.ids)]
            })
        return res
