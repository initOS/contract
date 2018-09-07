# Copyright 2018 Florian Kantelberg <florian.kantelberg@initos.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Contract Variable Formulas",
    "version": "11.0.1.0.0",
    "author": '''initOS GmbH,
                 Odoo Community Association (OCA)''',
    'category': 'Contract Management',
    'website': 'https://github.com/oca/contract',
    "depends": [
        "contract_variable_quantity",
    ],
    "license": "AGPL-3",
    "data": [
        "data/contract_line_qty_formula.xml",
    ],
    'installable': True,
}
