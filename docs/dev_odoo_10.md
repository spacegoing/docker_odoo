# Odoo 10 Dev Ess #

## Gotchas ##

### Chapter2 ###

- Error: @api.model somehow raised exceptions in odoo10

  ``` python
      @api.model
      def do_clear_done(self):
          dones = self.search(['is_done', '=', True])
          dones.write({'active':False})
          return True
  ```

- In test_todo.py, it was `Todo.do_clear_done()`. So I suspect
  that the `clear all done` button should be appeared in upper
  layer rather than the create/edit layer

## Q&A ##










