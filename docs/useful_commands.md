### Dev version ###

- Run odoo without `CMD [ "odoo" ]` and `entrypoint.sh`: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8069 --logfile=stdout"

- Run odoo with log file: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8069 --logfile=/var/log/odoo/odoo_inst1.log"

- Test: "odoo --test-enable -u todo_app --log-level=test --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8069 --logfile=stdout --stop-after-init"

### Official Distribute ###

- multi odoo instance: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"

- print command used to run `odoo-bin`: *ps -aux | awk '{ s = ""; for (i = 11; i <= 30; i++) s = s $i " "; print s }'*

- with updates (`todo_app` i'm developing): "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log -u todo_app"

  - note: `-u` command can follow comma separated module names
    `todo_app,mail ...`
  
- enable test: "odoo --db_host db --db_port 5432 -r odoo -w odoo -i todo_app --test-enable --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"
  
- enable test: "odoo --test-enable -i todo_app --log-level=test --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=stdout --stop-after-init"

