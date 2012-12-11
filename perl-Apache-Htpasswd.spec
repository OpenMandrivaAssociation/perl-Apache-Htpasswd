%define upstream_name    Apache-Htpasswd
%define upstream_version 1.8

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Manage Unix crypt-style password file
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Crypt::PasswdMD5)
BuildRequires:	perl(Digest::SHA1)
BuildRequires:	perl(MIME::Base64)

BuildArch:	noarch

%description
This module comes with a set of methods to use with htaccess password
files. These files (and htaccess) are used to do Basic Authentication on a
web server.

The passwords file is a flat-file with login name and their associated
crypted password. You can use this for non-Apache files if you wish, but it
was written specifically for .htaccess style files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.800.0-2mdv2011.0
+ Revision: 653388
- rebuild for updated spec-helper

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1.800.0-1mdv2011.0
+ Revision: 504564
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.8-1mdv2009.1
+ Revision: 291362
- import perl-Apache-Htpasswd


* Fri Oct 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.8-1mdv2009.1
- initial mdv release, generated with cpan2dist

