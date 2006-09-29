have webapp && {

# webapp(1) completion
#
_webapp()
{
	local cur prev

	COMPREPLY=()
	cur=${COMP_WORDS[COMP_CWORD]}
	prev=${COMP_WORDS[COMP_CWORD-1]}

	case "$COMP_CWORD" in
	1)
		COMPREPLY=($( compgen -W 'register unregister list list-apps' -- $cur ))
		;;
	2)
		case "$prev" in
		register|unregister|list)
			COMPREPLY=($( compgen -W 'apache httpd lighttpd' -- $cur ))
			;;
		esac
		;;
	3)
		case "${COMP_WORDS[COMP_CWORD-2]}" in
		register)
			COMPREPLY=($( compgen -W "$(webapp list-apps-unregistered $prev)" -- $cur ))
			;;
		unregister)
			COMPREPLY=($( compgen -W "$(webapp list-apps-registered $prev)" -- $cur ))
			;;
		esac
		;;
	esac

#	return 0
}

complete -F _webapp webapp
}
