### Dev version ###

- Dev odoo without `CMD [ "odoo" ]` and `entrypoint.sh`: 
  - "odoo -d db --db_host db --db_port 5432 --db_user odoo --db_password odoo --dev=all,ipdb --xmlrpc-port=8069"
  - "docker exec -it n bash"

- Dev odoo with log file: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8069 --logfile=/var/log/odoo/odoo_inst1.log"

- Test: "odoo -d db -u todo_app --test-enable --log-level=test --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8069 --stop-after-init"

- Run: 
  - "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8069 --log-level=info"

### Official Distribute ###

- multi odoo instance: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"

- print command used to run `odoo-bin`: *ps -aux | awk '{ s = ""; for (i = 11; i <= 30; i++) s = s $i " "; print s }'*

- with updates (`todo_app` i'm developing): "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log -u todo_app"

  - note: `-u` command can follow comma separated module names
    `todo_app,mail ...`
  
- enable test: "odoo --db_host db --db_port 5432 -r odoo -w odoo -i todo_app --test-enable --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"
  
- enable test: "odoo --test-enable -i todo_app --log-level=test --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=stdout --stop-after-init"

### Remove Volumes ###
- "docker volume rm `docker volume ls -q -f dangling=true`"

