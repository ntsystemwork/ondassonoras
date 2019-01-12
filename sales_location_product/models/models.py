# -*- coding: utf-8 -*-

import logging
from odoo import models, tools, fields, api, _

_logger = logging.getLogger(__name__)


class ProductTemplateLocation(models.Model):
    _inherit = "product.template"
    
    location_info_id = fields.Many2one('stock.location', string='Ubicacion física informativa', required=False,
                                       domain=[('usage', '=', 'internal')])

class ProductProductLocation(models.Model):
    _inherit = "product.product"
    
    location_info_id = fields.Many2one('stock.location', string='Ubicacion física informativa', required=False,
                                       domain=[('usage', '=', 'internal')])
