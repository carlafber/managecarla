#-*- coding: utf-8 -*-

from odoo import models, fields, api

class developer(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    is_dev = fields.Boolean(string="¿Es Desarrollador?", default=True)
    
    technologies_id = fields.Many2many(string = "Tecnologías", comodel_name = "managecarla.technology", 
                                       relation = "developer_technologies",
                                       column1 = "developer_id", column2 = "technologies")
   