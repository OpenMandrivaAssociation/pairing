Name:		pairing
Version:	1.3
Release:	2
Summary:	Pairing of machines for network testing
License:	GPL
Group:		Networking/Other
Url:		https://ahorvath.web.cern.ch/ahorvath/pairing/
Source:		%{name}-%{version}.tar.bz2

%description
Run this on a set of machines and get them paired up nicely for some
network-related activity.

It uses multicast to find potential partners and TCP to actually pair up with
them.

%prep
%setup -q

%build
make

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}/%{_bindir}
%__install -m 755 pair %{buildroot}/%{_bindir}/pair

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/pair



%changelog
* Wed Jan 25 2012 Andrey Bondrov <abondrov@mandriva.org> 1.3-1
+ Revision: 768190
- New version 1.3

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2010.0
+ Revision: 430230
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.1-3mdv2009.0
+ Revision: 241133
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Aug 07 2007 Erwan Velu <erwan@mandriva.org> 1.1-1mdv2008.0
+ Revision: 59788
- Import pairing

