Summary:	Ethernet settings tool for network cards
Name:		ethtool
Version:	3.8
Release:	1
License:	GPL
Group:		System/Configuration/Networking
Source0:	https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz
Source1:	https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.sign
URL:		https://www.kernel.org/pub/software/network/ethtool
Epoch:		1

%description
This utility allows querying and changing of ethernet
card settings, such as speed, port, and autonegotiation.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS NEWS
%{_mandir}/*/*
%{_sbindir}/ethtool
