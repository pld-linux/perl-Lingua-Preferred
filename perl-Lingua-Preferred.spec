#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	Preferred
Summary:	Lingua::Preferred - Perl extension to choose a language
Summary(pl):	Lingua::Preferred - rozszerzenie Perla do wybierania jêzyka
Name:		perl-Lingua-Preferred
Version:	0.2.4
Release:	1
# assuming same as perl, as not specified in sources
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	37e883fafb05b1439de1121f41e8ad75
BuildRequires:	perl-Log-TraceMessages >= 1.0
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Often human-readable information is available in more than one
language. Which should you use? This module provides a way for the
user to specify possible languages in order of preference, and then to
pick the best language of those available. Different 'dialects' given
by the 'territory' part of the language specifier (such as en, en_GB,
and en_US) are also supported.

%description -l pl
Czêsto informacje czytelne dla cz³owieka s± dostêpne w wiêcej ni¿
jednym jêzyku. Którego z nich nale¿y u¿yæ? Ten modu³ udostêpnia metodê
do przekazywania przez u¿ytkownika mo¿liwych jêzyków w kolejno¶ci
preferencji, a nastêpnie wyboru najlepszego jêzyka spo¶ród dostêpnych.
Ró¿ne "dialekty" podane przez czê¶æ "terytorialn±" okre¶lenia jêzyka
(takie jak en, en_GB i en_US) tak¿e s± obs³ugiwane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Lingua/*.pm
%dir %{perl_vendorlib}/auto/Lingua
%dir %{perl_vendorlib}/auto/Lingua/Preferred
%{perl_vendorlib}/auto/Lingua/Preferred/autosplit.ix
%{_mandir}/man3/*
