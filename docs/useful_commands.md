- print command used to run `odoo-bin`: *ps -aux | awk '{ s = ""; for (i = 11; i <= 30; i++) s = s $i " "; print s }'*

- multi odoo instance: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"

- with updates (`todo_app` i'm developing): "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log -u todo_app"

  - note: `-u` command can follow comma separated module names
    `todo_app,mail ...`
  
- enable test: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo -i todo_app --test-enable --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"
  
  