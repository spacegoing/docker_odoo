- print command used to run `odoo-bin`: "ps -aux | awk '{ s = ""; for (i = 11; i <= 30; i++) s = s $i " "; print s }'"

- multi odoo instance: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"
  
  
  
  