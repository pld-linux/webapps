Summary:	webapps framework
Summary(pl):	Szkielet dla aplikacji WWW
Name:		webapps
Version:	0.2
Release:	4
License:	GPL
Group:		Applications/WWW
Source0:	%{name}.sh
Source1:	%{name}.README
Requires:	webserver
Conflicts:	apache1 < 1.3.34-3.2
# can't conflict apache2 as apache1 is matched. just hope the best for now
#Conflicts:	apache < 2.0.55-2.2
Conflicts:	lighttpd < 1.4.7-2.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/webapps

%description
webapps is a package for having web applications configuration files
and webserver config fragments in unified place.

%description -l pl
webapps to pakiet pozwalaj±cy trzymaæ pliki konfiguracyjne aplikacji
WWW i fragmenty konfiguracji serwera WWW w jednym miejscu.

%prep
%setup -qcT
cp %{SOURCE1} README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}
install %{SOURCE0} $RPM_BUILD_ROOT%{_sbindir}/webapp

%triggerin -- apache < 2.0.55-2.2
if [ -d /etc/httpd ] && [ ! -d /etc/httpd/webapps.d ]; then
cat >&2 << 'EOF'
IMPORTANT:
 Your Apache 2.x is not webapps compatible!
 please upgrade your Apache 2.x installation to at least apache-2.0.55-2.2!
 (apache-2.0.55-3.2 should be in ac-ready)
EOF
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %attr(751,root,http) %{_sysconfdir}
%attr(755,root,root) %{_sbindir}/*
