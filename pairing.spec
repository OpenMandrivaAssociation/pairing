Name:		pairing
Version:	1.3
Release:	%mkrel 1
Summary:	Pairing of machines for network testing
License:	GPL
Group:		Networking/Other
Url:		http://ahorvath.web.cern.ch/ahorvath/pairing/
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

