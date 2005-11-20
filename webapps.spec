Summary:	webapps
Name:		webapps
Version:	0.1
Release:	0.2
License:	GPL
Group:		Applications/WWW
Source0:	%{name}.README
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/webapps

%description
webapps is a package for having web applications configuration files
and webserver config fragments in unified place.

webserver configs are in $webapps/$httpd
web application configs are in $webapps/configs/$webapp

individual directory for $webapps/$httpd is provided by webserver
itself.

%prep
cp %{SOURCE0} README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/config

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %attr(751,root,http) %{_sysconfdir}
%dir %attr(751,root,http) %{_sysconfdir}/config
