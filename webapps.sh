#!/bin/sh
webapps=/etc/webapps
action="$1"
httpd="$2"
app="$3"

webapp_register() {
	ln -sf $webapps/$app/$httpd.conf /etc/$httpd/webapps.d/$app.conf
}

webapp_unregister() {
	rm -f /etc/$httpd/webapps.d/$app.conf
}

usage() {
	cat >&2 <<EOF
Usage: $0 register httpd webapp
Usage: $0 unregister httpd webapp

Where httpd is one of the webservers
apache 1.x: apache
apache 2.x: httpd
lighttpd: lighttpd
EOF
}

die() {
	echo >&2 "$0: $*"
	exit 1
}

checkconfig() {
	# sanity check
	if [ ! -d "$webapps/$app" ]; then
		die "Missing directory: $webapps/$app"
	fi
	if [ ! -d "/etc/$httpd/webapps.d" ]; then
		die "Missing directory: /etc/$httpd/webapps.d"
	fi
}

case "$action" in
register)
	checkconfig
	webapp_register
	;;
unregister)
	checkconfig
	webapp_unregister
	;;
*)
	usage
	exit 1
esac
