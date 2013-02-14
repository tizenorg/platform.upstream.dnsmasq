Name:       dnsmasq
Summary:    dnsmasq, DNS forwarder.
Version:    2.57
Release:    6
Group:      TO_BE/FILLED_IN
License:    GPLv2
Source0:    %{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: pkgconfig(dbus-1)

%description
Dnsmasq is a lightweight, easy to configure DNS forwarder and DHCP server.

%prep
%setup -q

%build
cmake . -DCMAKE_INSTALL_PREFIX=%{_prefix}
make %{?jobs:-j%jobs}

%post
mkdir -p /opt/var/lib/misc

%install
rm -rf %{buildroot}
%make_install

%files
%manifest dnsmasq.manifest
%{_bindir}/dnsmasq

%changelog
* Tue Jan 15 2013 Seungyoun Ju <sy39.ju@samsung.com> 2.57-6
- Send the indication for DHCP connection every time

* Fri Nov 02 2012 Seungyoun Ju <sy39.ju@samsung.com> 2.57-5
- Default manifest file is added

* Mon Apr 16 2012 Seungyoun Ju <sy39.ju@samsung.com> 2.57-4
- "/opt/var/lib/misc" directory for lease file is created explicitly
