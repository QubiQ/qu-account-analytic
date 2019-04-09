# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    def _prepare_invoice_line_from_po_line(self, line):
        res = super(AccountInvoice, self)._prepare_invoice_line_from_po_line(
            line
        )
        res.update({
            'customer_id': line.customer_id.id,
            'provider_id': line.provider_id.id
        })
        return res

    @api.model
    def _prepare_invoice_line_data(self, line):
        res = super(AccountInvoice, self)._prepare_invoice_line_data(line)
        if line.customer_id and line.provider_id and line.analytic_tag_ids:
            res.update({
                'customer_id': line.customer_id.id,
                'provider_id': line.provider_id.id,
                'analytic_tag_ids': [(6, 0, line.analytic_tag_ids.ids)]
            })
        return res
