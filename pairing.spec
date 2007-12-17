%define name pairing
%define version 1.1
%define release %mkrel 1

Summary:   Pairing of machines for network testing
Name:      %name 
Version:   %version
Release:   %release
License:   GPL
Group:     Networking/Other
Source:    %{name}-%{version}.tar.bz2
Url:	   http://ahorvath.web.cern.ch/ahorvath/pairing/

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
mkdir -p %{buildroot}/%{_bindir}
install -m 755 pair %{buildroot}/%{_bindir}/pair

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/pair

%changelog
