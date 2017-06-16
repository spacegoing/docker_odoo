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
- `base` should be in `depends` when there is no other depends.
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



### Model Implementation ###

#### Derive from odoo.models.Model ####

- `_name` attribute defines the identifier that will be used
  through Odoo to refer to this `model` (model means MVC's M, not
  module). It will used by: 

  - views(`.xml` file `res_model`)
  
  todo: The class name meanlingness to other modules? dev ess P
  74

- In order the addon knows the module, it must be loaded in the
  `__init__.py`
  
  `from . import [**filename not _name, but then must use _name
  to import in other .py modules**]`

### View Implementation ###

- how each file related to views?
- Why no views even 3 records declared in todo_view.xml?
- Each record belongs to which part?

### Controller Implementation ###

- `do_clear_done` `@api.multi` raises error.





### Test ###

- Odoo use `Unittest2` to offer test func. The test file should
  start with `test_` and should be imported from
  `tests/__init__.py`. But `tests` dir shouldn't be imported from
  module's top `__init__.py`.

- enable test: "odoo --db_host db --db_port 5432 --db_user odoo --db_password odoo -i todo_app --test-enable --xmlrpc-port=8070 --logfile=/var/log/odoo/odoo_inst1.log"







## Gotchas ##

### CLI ###

- `-u` `-i` must be used with `-d (database name)` to take effect
- Somehow `dev=all,ipdb` doesn't take any effect in `.conf`. Have
  to explicitly declared in command line


### Test ###

- [`demo database` **Must** be installed. Otherwise test wouldn't run](https://www.odoo.com/forum/help-1/question/why-my-test-yaml-do-not-run-42123)
- https://github.com/camptocamp/pytest-odoo






## Todo: ##

### Docs ###

- `@api.model`

### Odoo shell ###

- https://webkul.com/blog/beginner-guide-odoo-clicommand-line-interface/



