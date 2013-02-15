Summary: Linux 802.1q VLAN configuration utility
Name: vconfig
Version: 1.9
Release: 14
License: GPLv2+
Group: System Environment/Base
Source: http://www.candelatech.com/~greear/vlan/vlan.%{version}.tar.gz
Source1001: %{name}.manifest
URL: http://www.candelatech.com/~greear/vlan.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%define _sbin /sbin

%description 
The vconfig program configures and adjusts 802.1q VLAN parameters.

%prep
%setup -q -n vlan.%{version}

%build
cp %{SOURCE1001} .
make clean
rm -f vconfig
make CCFLAGS="%{optflags}" STRIP=/bin/true vconfig

%install
rm -rf ${RPM_BUILD_ROOT}
%{__install} -D -m755 vconfig ${RPM_BUILD_ROOT}%{_sbin}/vconfig
%{__install} -D -m644 vconfig.8 ${RPM_BUILD_ROOT}%{_mandir}/man8/vconfig.8
rm -rf contrib/CVS

%clean 
rm -rf ${RPM_BUILD_ROOT}

%files 
%defattr(-, root, root, 0755)
%manifest %{name}.manifest
%doc CHANGELOG contrib README vlan.html vlan_test.pl
%{_sbin}/vconfig
%{_mandir}/man8/vconfig.8*
