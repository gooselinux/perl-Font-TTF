%global cpanname Font-TTF

Name:    perl-%{cpanname}
Version: 0.45
Release: 6%{?dist}
Summary: Perl library for modifying TTF font files

Group:     Development/Libraries
License:   Artistic 2.0
URL:       http://search.cpan.org/dist/%{cpanname}/
Source0:   http://cpan.org/authors/id/M/MH/MHOSKEN/%{cpanname}-%{version}.tar.gz
Source1:   %{name}-COPYING.Fedora
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch:     noarch
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: dos2unix
# Check requirements
BuildRequires: perl(Test::Simple)

Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl module for TrueType font hacking. Supports reading, processing and writing
of the following tables: GDEF, GPOS, GSUB, LTSH, OS/2, PCLT, bsln, cmap, cvt,
fdsc, feat, fpgm, glyf, hdmx, head, hhea, hmtx, kern, loca, maxp, mort, name,
post, prep, prop, vhea, vmtx and the reading and writing of all other table
types.

In short, you can do almost anything with a standard TrueType font with this
module.


%prep
%setup -q -n %{cpanname}-%{version}
dos2unix README.TXT COPYING lib/Font/TTF/Changes
install -m 0644 -p %{SOURCE1} COPYING.Fedora


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -fr %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -type f -name '*.bs' -a -size 0 -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

chmod -R u+rwX,g+rX %{buildroot}/*


%check
make test


%clean
rm -fr %{buildroot}


%files
%defattr(0644,root,root,0755)
%doc README.TXT COPYING COPYING.Fedora lib/Font/TTF/Changes

%dir %{perl_vendorlib}/Font
%dir %{perl_vendorlib}/Font/TTF

%{perl_vendorlib}/ttfmod.pl
%{perl_vendorlib}/Font/TTF.pm
%{perl_vendorlib}/Font/TTF/*

%exclude %{perl_vendorlib}/Font/TTF/Changes

%{_mandir}/man3/*.3*

# We really don't want to use this perl package in a Win32 env
# or poke in the windows registry to resolve fonts
# (upstream makefile needs to get smarter)
%exclude %{perl_vendorlib}/Font/TTF/Win32.pm


%changelog
* Fri Dec  4 2009 Stepan Kasal <skasal@redhat.com> - 0.45-6
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.45-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 23 2009 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.45-3
— global-ization

* Thu Sep 4 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.45-2
⚖ ⇒ Artistic 2.0

* Fri Jul 11 2008 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.45-1
⌖ Fedora 10 alpha general package cleanup
⚖ Upstream needs to relicense fast to avoid culling

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com>
- 0.43-3
Rebuild for new perl

* Sat Feb 09 2008  Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.43-2

* Fri May 18 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.41-1

* Tue Mar 20 2007 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.40.0-3
- small packaging fixes

* Sat Sep 02 2006  Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.40.0-2
- FE6 Rebuild

* Mon Jul 31 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.40.0-1

* Sat Feb 18 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.38.1-1
- new version with COPYING file as requested from upstream
  many thanks to Martin Hosken for quick action!

* Mon Feb 13 2006 Nicolas Mailhot <nicolas.mailhot at laposte.net>
- 0.37-4
- rebuilt for new gcc4.1 snapshot and glibc changes

* Sun Feb 5 2006 Nicolas Mailhot <nicolas.mailhot (at) laposte.net>
- 0.37-3
- spec cleanups #2

* Sun Feb 5 2006 Nicolas Mailhot <nicolas.mailhot (at) laposte.net>
- 0.37-2
- spec cleanups

* Sat Feb 4 2006 Nicolas Mailhot <nicolas.mailhot (at) laposte.net>
- 0.37-1
- Initial release
