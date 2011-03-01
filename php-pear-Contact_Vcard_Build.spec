%include	/usr/lib/rpm/macros.php
%define		_class		Contact_Vcard_Build
%define		_status		stable
%define		_pearname	%{_class}
Summary:	%{_pearname} - build (create) and fetch vCard 2.1 and 3.0 text blocks
Summary(pl.UTF-8):	%{_pearname} - tworzenie i wyciąganie bloków tekstu vCard 2.1 i 3.0
Name:		php-pear-%{_pearname}
Version:	1.1.2
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6df82ac23c3786e2e2a4b08e60cc6aa9
URL:		http://pear.php.net/package/Contact_Vcard_Build/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-Contact_Vcard_Build-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Allows you to programmatically create a vCard, version 2.1 or 3.0, and
fetch the vCard text.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Klasa pozwala na programowe tworzenie vCard w wersji 2.1 lub 3.0 oraz
wyciąganie tekstu z vCard.

Ta klasa ma w PEAR status: %{_status}.

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
%dir %{php_pear_dir}/Contact/Vcard
%{php_pear_dir}/Contact/Vcard/Build.php
