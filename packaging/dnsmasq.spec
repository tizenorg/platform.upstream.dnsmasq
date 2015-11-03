Name:           dnsmasq
Summary:        A lightweight DNS forwarder and DHCP server
Version:        2.57.1
Release:        0
Group:          Network & Connectivity/Data Network
License:        GPL-2.0
Source0:        %{name}-%{version}.tar.gz
Source1001:     dnsmasq.manifest
BuildRequires:  cmake
BuildRequires:  pkgconfig(dbus-1)

%description
Dnsmasq is a lightweight, easy to configure DNS forwarder and DHCP server.
It is designed to provide DNS and, optionally, DHCP, to a small network.
It can serve the names of local machines that are not in the global DNS.
The DHCP server integrates with the DNS server and allows machines with
DHCP-allocated addresses to appear in DNS with names configured either
in each host or in a central configuration file. Dnsmasq supports static
and dynamic DHCP leases and BOOTP for network booting of diskless machines.

%prep
%setup -q
cp %{SOURCE1001} .

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%post
mkdir -p /opt/var/lib/misc

%install
%make_install
mkdir -p %{buildroot}%{_sysconfdir}/dbus-1/system.d
cp dbus/dnsmasq.conf %{buildroot}%{_sysconfdir}/dbus-1/system.d/dnsmasq.conf

%files
%manifest %{name}.manifest
%{_bindir}/dnsmasq
%attr(644,root,root) %{_sysconfdir}/dbus-1/system.d/*
