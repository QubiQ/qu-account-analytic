# Copyright 2019 Xavier Piernas <xavier.piernas@qubiq.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Analytic Tag Product Partner",
    "summary": "Generates analytic tags from products and partners",
    "version": "12.0.1.0.0",
    "category": "Sales, Purchases, Invoicing",
    "website": "https://www.qubiq.es",
    "author": "QubiQ, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "account",
        "purchase",
        "sale",
        "inter_company_rules"
    ],
    "data": [
        "views/account_invoice.xml",
        "views/purchase_order.xml",
        "views/sale_order.xml"
    ],
}
