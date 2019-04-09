# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class StockRule(models.Model):
    _inherit = 'stock.rule'

    @api.multi
    def _prepare_purchase_order_line(
        self, product_id, product_qty, product_uom, values, po, partner
    ):
        res = super(StockRule, self)._prepare_purchase_order_line(
            product_id, product_qty, product_uom, values, po, partner
        )
        if values.get('move_dest_ids'):
            sale_line_id = values.get('move_dest_ids').sale_line_id
            res.update({
                'customer_id': sale_line_id.customer_id.id,
                'provider_id': sale_line_id.provider_id.id,
                'analytic_tag_ids': [(6, 0, sale_line_id.analytic_tag_ids.ids)]
            })
        return res
