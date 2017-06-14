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

#### Manifest File ####

- only `name` (app name) is required
- However, you should be careful to ensure all dependencies are
  explicitly set in `depends`. The module will fail to install or
  have loading errors if by chance the other required modules are
  loaded afterward.


### Dev Workflow ###

1. Install the module
2. After module installed, any changes in source code requires a
   restart of the odoo instance. Because Odoo loads python code
   only once.
   
   - `./odoo-bin -d todo -u todo_app`
















