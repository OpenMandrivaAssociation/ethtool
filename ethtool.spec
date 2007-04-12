Summary:	Ethernet settings tool for network cards
Name:		ethtool
Version:	5
Release:	%mkrel 1
License:	GPL
Group:		System/Configuration/Networking
Source:		http://prdownloads.sourceforge.net/gkernel/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://sourceforge.net/projects/gkernel/


%description
This utility allows querying and changing of ethernet
card settings, such as speed, port, and autonegotiation.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS NEWS
%{_mandir}/*/*
%{_sbindir}/ethtool


