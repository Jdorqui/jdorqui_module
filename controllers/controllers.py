# -*- coding: utf-8 -*-
# from odoo import http


# class JdorquiModule(http.Controller):
#     @http.route('/jdorqui_module/jdorqui_module', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jdorqui_module/jdorqui_module/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('jdorqui_module.listing', {
#             'root': '/jdorqui_module/jdorqui_module',
#             'objects': http.request.env['jdorqui_module.jdorqui_module'].search([]),
#         })

#     @http.route('/jdorqui_module/jdorqui_module/objects/<model("jdorqui_module.jdorqui_module"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jdorqui_module.object', {
#             'object': obj
#         })

