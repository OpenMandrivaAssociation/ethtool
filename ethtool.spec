%global optflags %{optflags} -Oz

Summary:	Ethernet settings tool for network cards
Name:		ethtool
Version:	6.14
Release:	1
License:	GPLv2
Group:		System/Configuration/Networking
Url:		https://www.kernel.org/pub/software/network/ethtool
Source0:	https://www.kernel.org/pub/software/network/ethtool/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libmnl)
BuildSystem:	autotools

%description
This utility allows querying and changing of ethernet
card settings, such as speed, port, and autonegotiation.

%files
%doc AUTHORS NEWS
%{_sbindir}/ethtool
%{_datadir}/bash-completion/completions/ethtool
%{_datadir}/metainfo/org.kernel.software.network.ethtool.metainfo.xml
%doc %{_mandir}/*/*
