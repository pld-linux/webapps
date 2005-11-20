Summary:	webapps framework
Summary(pl):	Szkielet dla aplikacji WWW
Name:		webapps
Version:	0.1
Release:	0.6
License:	GPL
Group:		Applications/WWW
Source0:	%{name}.sh
Source1:	%{name}.README
Conflicts:	apache1 < 1.3.34-3.2
# can't conflict apache2 as apache1 is matched.
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
%setup -q -c -T
cp %{SOURCE0} README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_sbindir}}
install %{SOURCE0} $RPM_BUILD_ROOT%{_sbindir}/webapp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %attr(751,root,http) %{_sysconfdir}
%attr(755,root,root) %{_sbindir}/*
