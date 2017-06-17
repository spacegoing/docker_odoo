#!/bin/bash

set -e

# set the postgres database host, port, user and password according to the environment
# and pass them as arguments to the odoo process if not present in the config file
: ${HOST:=${DB_PORT_5432_TCP_ADDR:='db'}}
: ${PORT:=${DB_PORT_5432_TCP_PORT:=5432}}
: ${USER:=${DB_ENV_POSTGRES_USER:=${POSTGRES_USER:='odoo'}}}
: ${PASSWORD:=${DB_ENV_POSTGRES_PASSWORD:=${POSTGRES_PASSWORD:='odoo'}}}

# DB_ARGS=()
# function check_config() {
#     param="$1"
#     value="$2"
#     if ! grep -q -E "^\s*\b${param}\b\s*=" "$ODOO_RC" ; then
#         DB_ARGS+=("--${param}")
#         DB_ARGS+=("${value}")
#    fi;
# }
# check_config "db_host" "$HOST"
# check_config "db_port" "$PORT"
# check_config "db_user" "$USER"
# check_config "db_password" "$PASSWORD"

# todo: Bad implementation. recreate every login
# -n will not already exists symlinks (otherwise will create symlink in those symlinks)
# -f will override existing symlinks
ln -snf /etc/odoo /var/lib/odoo/config_odoo
ln -snf /mnt/extra-addons /var/lib/odoo/extra-addons
ln -snf /usr/lib/python2.7/dist-packages/odoo /var/lib/odoo/src_odoo


case "$1" in
    # -- | odoo)
    #     shift
    #     if [[ "$1" == "scaffold" ]] ; then
    #         exec odoo "$@"
    #     else
    #         exec odoo "$@" "${DB_ARGS[@]}"
    #     fi
    #     ;;
    # -*)
    #     exec odoo "$@" "${DB_ARGS[@]}"
    #     ;;
    *)
        exec "$@"
esac

# FixMe: shouldn't without exit code
# exit 1
