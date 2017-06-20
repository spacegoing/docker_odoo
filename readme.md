## My Odoo Dev Env ##

- pip 9.0+ installed
- ipython 5.4+ installed; ipdb installed
- latest(nightly) odoo deb build into image
- run `bash` as entrypoint rather than `odoo` for dev's
  convenient
- Useful dirs already symlinked to home (`/var/lib/odoo`)
- Useful bash commands (in container) in favor of `odoo` dev

## Run ##

- docker-compose up -d
- docker ps
- dbash (my private bash command) container_id [container_id]

### spacemacs Usage ###

Be sure you are at Emacs 25.2 with `docker-layer` installed.

After `docker-compose up -d`

- `SPC f f` to open `HELM Find Files`
- Input `/docker:odoodocker_web_1:`, this will invoke `tramp`
  using `docker ssh`. If success, helm should prompt
  `/docker:odoodocker_web_1:/var/lib/odoo/` in popups. Enter that
  directory 
- There are symlinks defined in `./entrypoint.sh`

## Odoo Init ##

- username, dbname, db password etc should all be `"db"`
- Important! load demo database. Otherwise `--test-enable` won't work

## Containers' Bash Commands ##

- `bare_odoo`: start odoo service without any dev options (logs,
  devmode etc.)
- `dev_odoo`: start odoo service with `dev=all,ipdb`
- `tapp_odoo`: test app. Takes 1 argument, a list of app names
  separated by `","`
- `tlapp_odoo`: test app with log. Doesn't work yet
















