#-*- coding: utf-8 -*-

from odoo import models, fields, api

class technology(models.Model):
    _name = 'managecarla.technology'
    _description = 'managecarla.technology'
    
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    image = fields.Image(string="Imagen", max_width=1024, max_height=1024)
    
    tasks_id = fields.Many2many(string = "Tareas", comodel_name = "managecarla.task", 
                                    relation = "tecnologias_tareas", column1 = "tareas_ids", column2 = "tecnologias_ids")