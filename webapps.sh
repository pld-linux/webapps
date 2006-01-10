#!/bin/sh

webapps=/etc/webapps
webservers='apache httpd lighttpd'
action="$1"
httpd="$2"
app="$3"

webapp_link() {
	echo "$1" | tr '/' '-'
}

webapp_register() {
	local link=$(webapp_link $app)
	ln -sf ../../..$webapps/$app/$httpd.conf /etc/$httpd/webapps.d/$link.conf
}

webapp_unregister() {
	local link=$(webapp_link $app)
	rm -f /etc/$httpd/webapps.d/$link.conf
}

webapp_list() {
	echo "registered webapps${1:+ for $1}":
	for server in ${1:-$webservers}; do
		[ -d /etc/$server/webapps.d ] || continue
		echo "$server:"
		for conf in /etc/$server/webapps.d/*; do
			[ -L $conf ] || continue
			app=$(basename $conf .conf)
			echo "- $app"
		done
	done
}

webapp_list_apps() {
	echo "available webapps${1:+ for $1}":
	for app in /etc/webapps/*; do
		[ -d $app ] || continue

		servers=""
		for server in ${1:-$webservers}; do
			[ -f $app/$server.conf ] || continue
			servers="$servers${servers:+ }$server"
		done

		[ "$servers" ] || continue
		echo "- $(basename $app) ($servers)"
	done
}

usage() {
	cat >&2 <<EOF
Usage: $0 register httpd webapp
Usage: $0 register httpd webapp/module
Usage: $0 unregister httpd webapp
Usage: $0 unregister httpd webapp/module
Usage: $0 list [$webservers]
Usage: $0 list-apps [$webservers]

Where httpd is one of the webservers
apache 1.x: apache
apache 2.x: httpd
lighttpd: lighttpd

webapp modules are supported,
"drupal tinymce" module webapp name would be "drupal/tinymce".
EOF
}

die() {
	echo >&2 "$0: $*"
	exit 1
}

checkconfig() {
	if [ -z "$httpd" ] || [ -z "$app" ]; then
		usage
		return 1
	fi

	# sanity check
	if [ ! -d "$webapps/$app" ]; then
		die "'$app' is not webapp? (Missing directory: $webapps/$app)"
	fi
	if [ ! -d "/etc/$httpd/webapps.d" ]; then
		die "'$httpd' is not a webserver? (Missing directory: /etc/$httpd/webapps.d)"
	fi
}

case "$action" in
register)
	checkconfig && webapp_register
	;;
unregister)
	checkconfig && webapp_unregister
	;;
list)
	webapp_list $2
	;;
list-apps)
	webapp_list_apps $2
	;;
*)
	usage
	exit 1
esac
