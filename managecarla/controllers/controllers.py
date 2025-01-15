# -*- coding: utf-8 -*-
# from odoo import http


# class Managecarla(http.Controller):
#     @http.route('/managecarla/managecarla', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/managecarla/managecarla/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('managecarla.listing', {
#             'root': '/managecarla/managecarla',
#             'objects': http.request.env['managecarla.managecarla'].search([]),
#         })

#     @http.route('/managecarla/managecarla/objects/<model("managecarla.managecarla"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('managecarla.object', {
#             'object': obj
#         })
