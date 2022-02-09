# -*- coding: utf-8 -*-
from odoo import http


class VehicleService(http.Controller):
    @http.route('/vehicle_service/vehicle_service/', auth='public')
    def index(self, **kw):
        return "Hello, world"
    @http.route('/vehicle_service/vehicle_service/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('vehicle_service.listing', {
            'root': '/vehicle_service/vehicle_service',
            'objects': http.request.env['vehicle_service.vehicle_service'].search([]),
        })

    @http.route('/vehicle_service/vehicle_service/objects/<model("vehicle_service.vehicle_service"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('vehicle_service.object', {
            'object': obj
        })
