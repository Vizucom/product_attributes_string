# -*- coding: utf-8 -*-
import openerp.addons.decimal_precision as dp
from openerp import models, fields, api, _


class ProductProduct(models.Model):

    _inherit = 'product.product'

    @api.multi
    def _compute_variant_human_readable(self):
        '''Create a comma-separated list of the product's attribute values (e.g. "Green, XL")
        To be utilized in e.g. Point of Sale or Aeroo Reports'''
        for product in self:
            attrs = []
            for attribute in product.attribute_value_ids:
                attrs.append(attribute.name)

            product.variant_human_readable = attrs and ", ".join(attrs) or ''

    variant_human_readable = fields.Char('Attribute list', compute='_compute_variant_human_readable')