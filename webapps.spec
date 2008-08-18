Summary:	webapps framework
Summary(pl.UTF-8):	Szkielet dla aplikacji WWW
Name:		webapps
Version:	0.3
Release:	4
License:	GPL
Group:		Applications/WWW
Source0:	%{name}.README
Source1:	%{name}.sh
Source2:	webapp-bash_completion.sh
Requires:	coreutils
Requires:	webserver
Conflicts:	apache < 2.0.55-2.2
Conflicts:	apache1 < 1.3.34-3.2
Conflicts:	lighttpd < 1.4.7-2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/webapps
%define		_bashcompletiondir	/etc/bash_completion.d

%description
webapps is a package for having web applications configuration files
and webserver config fragments in unified place.

%description -l pl.UTF-8
webapps to pakiet pozwalający trzymać pliki konfiguracyjne aplikacji
WWW i fragmenty konfiguracji serwera WWW w jednym miejscu.

%package -n bash-completion-webapps
Summary:	bash completion for webapps
Summary(pl.UTF-8):	Dopełnienia basha dla webapps
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion

%description -n bash-completion-webapps
Bash completion for webapps.

%description -n bash-completion-webapps -l pl.UTF-8
Dopełnienia basha dla webapps.

%prep
%setup -qcT
cp %{SOURCE0} README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir},%{_bashcompletiondir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_sbindir}/webapp
install %{SOURCE2} $RPM_BUILD_ROOT%{_bashcompletiondir}/webapp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %attr(751,root,http) %{_sysconfdir}
%attr(755,root,root) %{_sbindir}/*

%files -n bash-completion-webapps
%defattr(644,root,root,755)
%{_bashcompletiondir}/webapp
