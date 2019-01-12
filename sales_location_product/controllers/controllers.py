# -*- coding: utf-8 -*-
from odoo import http

# class ../../argentina/importProductEcommerce(http.Controller):
#     @http.route('/../../argentina/import_product_ecommerce/../../argentina/import_product_ecommerce/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/../../argentina/import_product_ecommerce/../../argentina/import_product_ecommerce/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('../../argentina/import_product_ecommerce.listing', {
#             'root': '/../../argentina/import_product_ecommerce/../../argentina/import_product_ecommerce',
#             'objects': http.request.env['../../argentina/import_product_ecommerce.../../argentina/import_product_ecommerce'].search([]),
#         })

#     @http.route('/../../argentina/import_product_ecommerce/../../argentina/import_product_ecommerce/objects/<model("../../argentina/import_product_ecommerce.../../argentina/import_product_ecommerce"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('../../argentina/import_product_ecommerce.object', {
#             'object': obj
#         })