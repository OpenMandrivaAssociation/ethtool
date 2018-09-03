Summary:	Ethernet settings tool for network cards
Name:		ethtool
Epoch:		1
Version:	4.18
Release:	1
License:	GPLv2
Group:		System/Configuration/Networking
Url:		https://www.kernel.org/pub/software/network/ethtool
Source0:	https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz

%description
This utility allows querying and changing of ethernet
card settings, such as speed, port, and autonegotiation.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS NEWS
%{_mandir}/*/*
%{_sbindir}/ethtool
