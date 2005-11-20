#!/bin/sh
webapps=/etc/webapps
action="$1"
httpd="$2"
app="$3"

webapp_register() {
	ln -sf $webapps/$app/$httpd.conf /etc/$httpd/webapps/$app.conf
}

webapp_unregister() {
	rm -f /etc/$httpd/webapps/$app.conf
}

usage() {
	cat >&2 <<EOF
Usage: $0 register httpd webapp
Usage: $0 unregister httpd webapp

Where httpd one of the webservers
apache 1.x: apache
apache 2.x: httpd
lighttpd: lighttpd
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
