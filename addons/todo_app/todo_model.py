# -*- coding: utf-8 -*-
from odoo import models, fields, api


class TodoTask(models.Model):
    # dev ess p75 in database modules todo.task
    _name = 'todo.task'
    _description = 'To-do Task'

    # special filed names
    # TODO: how to use name?
    name = fields.Char('Description', required=True)
    active = fields.Boolean('Active?', default=True)
    is_done = fields.Boolean('Done?')

    @api.multi
    def do_toggle_done(self):
        for task in self:
            task.is_done = not task.is_done
        return True

    @api.model
    def do_clear_done(self):
        dones = self.search(['is_done', '=', True])
        dones.write({'active':False})
        return True













