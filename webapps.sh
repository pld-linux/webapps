#!/bin/sh
webapps=/etc/webapps
action="$1"
webserver="$2"
app="$3"

webapp_register() {
	ln -sf $webapps/$app/$webserver.conf /etc/$webserver/webapps/$app.conf
}

webapp_unregister() {
	rm -f /etc/$webserver/webapps/$app.conf
}

usage() {
	cat >&2 <<EOF
Usage: $0 register webserver webapp
Usage: $0 unregister webserver webapp
EOF
}

case "$action" in
register)
	webapp_register
	;;
unregister)
	webapp_unregister
	;;
*)
	usage
	exit 1
esac
