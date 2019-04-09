# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    @api.model
    def _prepare_sale_order_line_data(self, line, company, sale_id):
        res = super(PurchaseOrder, self)._prepare_sale_order_line_data(
            line, company, sale_id
        )
        if line.customer_id and line.provider_id and line.analytic_tag_ids:
            res.update({
                'customer_id': line.customer_id.id,
                'provider_id': line.provider_id.id,
                'analytic_tag_ids': [(6, 0, line.analytic_tag_ids.ids)]
            })
        return res
