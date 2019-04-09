# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    customer_id = fields.Many2one(
        comodel_name='res.partner',
        string=_('Customer')
    )
    provider_id = fields.Many2one(
        comodel_name='res.partner',
        string=_('Provider')
    )

    @api.onchange('product_id', 'customer_id', 'provider_id')
    def onchange_product_id_customer_id_provider_id(self):
        analytic_tag_id = False
        if self.product_id and self.customer_id and self.provider_id and\
                self.product_id.default_code and self.customer_id.ref and\
                self.provider_id.ref:
            name = self.product_id.default_code + '-' + self.customer_id.ref +\
                self.provider_id.ref
            analytic_tag_id = self.env['account.analytic.tag'].search([
                ('name', '=', name)
            ], limit=1)
            if not analytic_tag_id:
                analytic_tag_id = self.env['account.analytic.tag'].create({
                    'name': name
                })
        self.analytic_tag_ids = analytic_tag_id

    @api.multi
    def _prepare_invoice_line(self, qty):
        res = super(SaleOrderLine, self)._prepare_invoice_line(qty)
        res.update({
            'customer_id': self.customer_id.id,
            'provider_id': self.provider_id.id
        })
        return res
