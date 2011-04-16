%define upstream_name    Apache-Htpasswd
%define upstream_version 1.8

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Manage Unix crypt-style password file
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Apache/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Crypt::PasswdMD5)
BuildRequires: perl(Digest::SHA1)
BuildRequires: perl(MIME::Base64)

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README
%{_mandir}/man3/*
%perl_vendorlib/*
