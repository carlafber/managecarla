#-*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class sprint(models.Model):
    _name = 'managecarla.sprint'
    _description = 'managecarla.sprint'
    
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    duration = fields.Integer(string = "Duración", default = 15)
    start_date = fields.Datetime(string="Fecha de inicio")
    end_date = fields.Datetime(string="Fecha de fin", compute = "_get_end_date", store = True)
        
    tasks_id = fields.One2many(string = "Tareas", comodel_name = "managecarla.task", inverse_name = "sprint_id")
    
    project_id = fields.Many2one("managecarla.project", string = "Proyecto", required = True, ondelete = "cascade")
    
    
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for sprint in self:
            if isinstance(sprint.start_date, datetime.datetime) and sprint.duration > 0:
                sprint.end_date = sprint.start_date + datetime.timedelta(days=sprint.duration)
            else:
                sprint.end_date = sprint.start_date    