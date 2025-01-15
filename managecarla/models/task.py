#-*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class task(models.Model):
    _name = 'managecarla.task'
    _description = 'managecarla.task'
    
    code = fields.Char(string="Código", compute = "_get_code")
    name = fields.Char(string="Nombre", readonly = False, required = True, help = "Introduzca el nombre")
    description = fields.Text(string="Descripción")
    start_date = fields.Datetime(string="Fecha de inicio", default = lambda p : datetime.datetime.now())
    end_date = fields.Datetime(string="Fecha de fin")
    is_paused = fields.Boolean(string="¿Pausada?")
    
    state = fields.Selection([
        ('todo', 'Por Hacer'),
        ('in_progress', 'En Progreso'),
        ('blocked', 'Bloqueada'),
        ('done', 'Completada')
    ], string="Estado", default='todo', required=True)
    
    
    sprint_id = fields.Many2one("managecarla.sprint", string = "Carrera", ondelete = "cascade", compute = "_get_sprint")

    technologies_id = fields.Many2many(string = "Tecnologías", comodel_name = "managecarla.technology", relation = "tecnologias_tareas", 
                                   column1 = "tecnologias_ids", column2 = "tareas_ids")
    
    history_id = fields.Many2one("managecarla.history", string = "Historia", required = True, ondelete = "cascade")
    
    project = fields.Many2one("managecarla.project", related = "history_id.project_id", readonly = True)
    
    
    def _get_code(self):
        for task in self:
            task.code = "TSK_" + str(task.id)
            
            
    #@api.depends('code')
    def _get_sprint(self):
        for task in self:
            sprints = self.env['managecarla.sprint'].search([('project_id', '=', task.history_id.project_id.id)])
            found = False
            for sprint in sprints:
                if isinstance(sprint.end_date, datetime.datetime) and sprint.end_date > datetime.datetime.now():
                    task.sprint_id = sprint.id
                    found = True
            if not found:
                task.sprint_id = False

    '''def _get_definition_date(self):
            return datetime.datetime.now()
        
    definition_date = fields.Datetime(string = "Fecha definición tarea", default = _get_definition_date)'''