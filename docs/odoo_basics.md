# Odoo Basics #

## Local Installation ##

- Install
``` bash
mkdir ~/ odoo-dev
git clone [odoo_repo] odoo-dev
cd odoo-dev/odoo/setup/setup_dev.py setup_deps
cd odoo-dev/odoo/setup/setup_dev.py setup_pg
```

- Run

``` bash
~/odoo-dev/odoo/odoo-bin
```














## Developing ##

### Init Project ###

- `odoo-bin scaffold --help` this can automatically generate
  basic structure of odoo modules. 
- `__manifest__.py`: a descriptor file. **An Odoo addon module is
  a directory containing a `manifest.py` file.**
  (`__openerp.py__` in previous versions). 
- `module name`: the `directory name` is its technical name. Only
  with letters, numbers, underscore.
- Don't forget `__init__.py`






