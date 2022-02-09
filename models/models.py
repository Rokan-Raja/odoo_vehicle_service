# -*- coding: utf-8 -*-

from odoo import models, fields, api


class vehicle_service(models.Model):
    _name = 'vehicle_service.vehicle_service'
    _description = 'vehicle_service.vehicle_service'
    name = fields.Char()
    vehicle_no = fields.Integer()
    phone = fields.Text()
    vehicle_type = fields.Selection([('2wheeler', '2wheeler'),
                                     ('3wheeler', '3wheeler'),
                                     ('4wheeler', '4wheeler')])

    service_type = fields.Selection([('Water_wash', 'Water_wash'),
                                     ('Dent_removal', 'Dent_removal'),
                                     ('Tyre_change', 'Tyre_change')])
    price = fields.Float(compute="_value_pc", store=True)
    @api.depends('service_type')
    def _value_pc(self):
        for record in self:
            if record.service_type == "Water_wash":
                a = 1000
                record.price = a
            if record.service_type == "Dent_removal":
                a = 500
                record.price = a
            if record.service_type == "Tyre_change":
                a = 1200
                record.price = a


