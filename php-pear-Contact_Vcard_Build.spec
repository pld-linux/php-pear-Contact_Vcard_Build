%include	/usr/lib/rpm/macros.php
%define         _class          Contact_Vcard_Build
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - Build (create) and fetch vCard 2.1 and 3.0 text blocks
Summary(pl):	%{_pearname} - tworzenie i wyci±ganie bloków tekstu vCard 2.1 i 3.0
Name:		php-pear-%{_pearname}
Version:	1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	88e92bb1f0d988c29b9f2645f41e5b5e
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to programmatically create a vCard, version 2.1 or 3.0, and
fetch the vCard text.

This class has in PEAR status: %{_status}.

%description -l pl
Klasa pozwala na programowe tworzenie vCard w wersji 2.1 lub 3.0 oraz
wyci±ganie tekstu z vCard.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}
%{php_pear_dir}/%{_class}/*.php
