#-*- coding: utf-8 -*-

from odoo import models, fields, api

class history(models.Model):
    _name = 'managecarla.history'
    _description = 'managecarla.history'
    
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    
    
    project_id = fields.Many2one("managecarla.project", string = "Proyecto", required = True, ondelete = "cascade")

    tasks_id = fields.One2many(string = "Tareas", comodel_name = "managecarla.task", inverse_name = "history_id")

    used_technologies = fields.Many2many("managecarla.technology", string = "Tecnologías utilizadas", compute = "_get_used_technologies")
    
    
    def _get_used_technologies(self):
        for history in self:
            technologies = None
            for task in history.tasks_id:
                if not technologies:
                    technologies = task.technologies_id
                else:
                    technologies = technologies + task.technologies_id
            history.used_technologies = technologies