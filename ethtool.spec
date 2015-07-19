Summary:	Ethernet settings tool for network cards
Name:		ethtool
Epoch:		1
Version:	3.18
Release:	2
License:	GPLv2
Group:		System/Configuration/Networking
Url:		https://www.kernel.org/pub/software/network/ethtool
Source0:	https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz

%description
This utility allows querying and changing of ethernet
card settings, such as speed, port, and autonegotiation.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS
%{_mandir}/*/*
%{_sbindir}/ethtool
