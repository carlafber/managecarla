#-*- coding: utf-8 -*-

from odoo import models, fields, api

class project(models.Model):
    _name = 'managecarla.project'
    _description = 'managecarla.project'
    
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    state = fields.Selection([
        ('todo', 'Por Hacer'),
        ('in_progress', 'En Progreso'),
        ('blocked', 'Bloqueado'),
        ('done', 'Completado')
    ], string="Estado", default='todo', required=True)
    progress = fields.Float(string="Progreso (%)", compute="_compute_progress", store=True)
    
    
    histories_id = fields.One2many(string = "Historias", comodel_name = "managecarla.history", inverse_name = "project_id")
    
    sprints_id = fields.One2many(string = "Carreras", comodel_name = "managecarla.sprint", inverse_name = "project_id")
    
    @api.depends('histories_id.tasks_id.state')
    def _compute_progress(self):
        for project in self:
            total_tasks = sum(len(history.tasks_id) for history in project.histories_id)
            completed_tasks = sum(len(history.tasks_id.filtered(lambda t: t.state == 'done')) for history in project.histories_id)
            in_progress_tasks = sum(len(history.tasks_id.filtered(lambda t: t.state == 'in_progress')) for history in project.histories_id)
            #carcular progreso
            project.progress = ((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0
            #actualizar estado
            if completed_tasks == total_tasks:
                project.state = 'done'
            elif in_progress_tasks > 0:
                project.state = 'in_progress'
            else:
                project.state = 'todo'