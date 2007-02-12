#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Model-DBIC
Summary:	Catalyst::Model::DBIC - DBIx::Class Model Class
Summary(pl.UTF-8):   Catalyst::Model::DBIC - klasa modelu DBIx::Class
Name:		perl-Catalyst-Model-DBIC
Version:	0.13
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c8a06cf175b6e4ec6567cb1311af41f6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.00
BuildRequires:	perl-DBIx-Class-Loader
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the DBIx::Class model class for Catalyst web application
framework. It's built on top of DBIx::Class::Loader.

%description -l pl.UTF-8
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
