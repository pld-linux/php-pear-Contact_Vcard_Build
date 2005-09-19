%include	/usr/lib/rpm/macros.php
%define		_class		Contact_Vcard_Build
%define		_status		stable
%define		_pearname	%{_class}

Summary:	%{_pearname} - build (create) and fetch vCard 2.1 and 3.0 text blocks
Summary(pl):	%{_pearname} - tworzenie i wyci±ganie bloków tekstu vCard 2.1 i 3.0
Name:		php-pear-%{_pearname}
Version:	1.1.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	c22cfac5cdade9116c26644f25c33d96
URL:		http://pear.php.net/package/Contact_Vcard_Build/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to programmatically create a vCard, version 2.1 or 3.0, and
fetch the vCard text.

In PEAR status of this package is: %{_status}.

%description -l pl
Klasa pozwala na programowe tworzenie vCard w wersji 2.1 lub 3.0 oraz
wyci±ganie tekstu z vCard.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
