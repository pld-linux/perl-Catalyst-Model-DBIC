#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Model-DBIC
Summary:	Catalyst::Model::DBIC - (DEPRECATED) DBIx::Class Model Class
Summary(pl.UTF-8):	Catalyst::Model::DBIC - (PRZESTARZAŁA) klasa modelu DBIx::Class
Name:		perl-Catalyst-Model-DBIC
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4ce5bd774dcbb64cb34a01f52801dc42
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.00
BuildRequires:	perl-DBIx-Class-Loader
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module has been deprecated in favor of the schema-based
Catalyst::Model::DBIC::Schema.

This is the DBIx::Class model class for Catalyst web application
framework. It's built on top of DBIx::Class::Loader.

%description -l pl.UTF-8
Ten moduł jest przestarzały, zastępuje go Catalyst::Model::DBIC::Schema.

To jest klasa modelu DBIx::Class dla szkieletu aplikacji WWW Catalyst.
Jest zbudowana w oparciu o DBIx::Class::Loader.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Model/*.pm
%{perl_vendorlib}/Catalyst/Helper/Model/*.pm
%{_mandir}/man3/*
